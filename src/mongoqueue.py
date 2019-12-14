from datetime import datetime, timedelta
from pymongo import MongoClient, errors

class MongoQueue:
    """
    >>> timeout = 1
    >>> url = "http://example.webscraping.com"
    >>> q = MongoQueue(timeout=timeout)
    >>> q.clear() # ensure empty queue
    >>> q.push(url) # add test URL
    >>> q.peek() == q.pop() == url # pop back this URL
    True
    >>> q.repair() # immediate repair will do nothin
    >>> q.pop() # another pop should be empty
    >>> q.peek() 
    >>> import time; time.sleep(timeout) # wait for timeout
    >>> q.repair() # now repair will release URL
    Released: test
    >>> q.pop() == url # pop URL again
    True
    >>> bool(q) # queue is still active while outstanding
    True
    >>> q.complete(url) # complete this URL
    >>> bool(q) # queue is not complete
    False
    """

    # possible states of a download
    outstanding, processing, complete = range(3)

    def __init__(self, client=None, timeout=300):
        """
        host: the host to connect to MongoDB
        port: the port to connect to MongoDB
        timeout: the number of seconds to allow for a timeout
        """
        self.client = MongoClient() if client is None else client
        self.db = self.client.cache
        self.timeout = timeout

    def __nonzero__(self):
        """
        Returns True if there are more jobs to process.
        """
        record = self.db.crawl_queue.find_one(
            {"status": {"$ne": self.complete}} 
        )
        return True if record else False

    def push(self, url):
        """
        Add new URL to queue if does not exist.
        """
        try:
            self.db.crawl_queue.insert({"_id": url, "status": self.outstanding})
        except errors.DuplicateKeyError as e:
            pass # this is already in the queue

    def pop(self):
        """
        Get an outstanding URL from the queue and set its status to processing.
        If the queue is empty a KeyError exception is raised.
        """
        record = self.db.crawl_queue.find_and_modify(
            query={"status": self.outstanding}, 
            update={"$set": {"status": self.processing, "timestamp": datetime.now()}}
        )
        if record:
            return record["_id"]
        else:
            self.repair()
            raise KeyError()

    def peek(self):
        """
        Peek at the ID for each record.
        """
        record = self.db.crawl_queue.find_one({"status": self.outstanding})
        if record:
            return record["_id"]

    def complete(self, url):
        """
        Mark the item in queue as completed.        
        """
        self.db.crawl_queue.update({"_id": url}, {"$set": {"status": self.complete}})

    def repair(self):
        """
        Release stalled jobs.
        """
        record = self.db.crawl_queue.find_and_modify(
            query={
                "timestamp": {"$lt": datetime.now() - timedelta(seconds=self.timeout)},
                "status": {"$ne": self.complete}
            },
            update={"$set": {"status": self.outstanding}}
        )
        if record:
            print "Released:", record["_id"]

    def clear(self):
        """
        Clear the queue.
        """
        self.db.crawl_queue.drop()

