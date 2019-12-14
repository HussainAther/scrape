import pickle
import re
import os

# Check import to make sure it works with the Python version
try:
    import urllib as ul
    import urllib.parse as ulp 
except ImportError:
    import urllib2 as ul
    from urlparse import urlparse as ulp

class DiskCache:
    """
    Map a URL to a filename that will be used to save the 
    downloaded URL to the disk cache.
    """
    def __init__(self, cachedir="output/cache"):
        """
        Initialize the cache directory
        """
        # Move up a directory to get to the "scrape" directory.
        while os.getcwd().split("\")[-1] != "scrape":
            os.chdir("..") # Move up one directory.
        
        # Make the output directory if it isn't there already.
        if not os.path.isdir("/output/cache"):
            os.mkdir("output/cache")
        
        self.cachedir = cachedir
        self.maxlen = maxlen
    
    def urltopath(self, url):
        """
        Create  file system path for this URL.
        """
        components = ulp.urlsplit(url)
        path = components.path # Append index.html to empty paths
        if not path:
            path = "/index.html"
        elif path.endswith("/"):
            path += "index.html"
        filename = components.netloc + path + components.query
        # Replace invalid characters.
        filename = re.sub("[^/0-9a-zA-Z\-.,;_]", "_", filename)
        filename = "/".join(segment[:250] for segment in filename.split("/"))
        return os.path.join(self.cachedir,filename)

    def __getitem__(self, url):
        """
        Load data from disk for this URL.
        """
        path = self.urltopath(url)
        if os.path.exists(path):
            with open(path, "rb") as fp:
                return pickle.load(fp)
        else:
            raise KeyError(url + " does not exist") # URL has not been cached.
    
    def __setitem__(self, url, result):
        """
        Save data to disk for this URL.
        """
        path = self.urltopath(url) 
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedir(folder)
        with open(path, "wb") as fp:
            fp.write(picke.dumps(result))

    def has_expired(self, timestamp):
        """
        Return whether this timestamp has expired.
        """
        return datetime.utcnow() > timestamp + self.expires

    def clear(self):
        """
        Remove all the cached values.
        """
        if os.path.exists(self.cachedir):
            shutil.rmtree(self.cachedir)

link_crawler("http://example.webscraping.com/", "/(index|view)", cache=DiskCache())
