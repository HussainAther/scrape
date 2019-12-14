# -*- coding: utf-8 -*-

import csv

from zipfile import ZipFile
from StringIO import StringIO
from mongocache import MongoCache

class AlexaCallback:
    """
    Callback function for the top sites on the Alexa rank.
    """
    def __init__(self, maxurls=1000):
        """
        Initialize the max number of urls
        and the Alexa rankings themselves.
        """
        self.maxurls = maxurls
        self.seed_url = "http://s3.amazonaws.com/alexa-static/top-1m.csv.zip"

    def __call__(self, url, html):
        """
        Callback function on the URL and HTML content.
        """
        if url == self.seed_url:
            urls = []
            cache = MongoCache()
            with ZipFile(StringIO(html)) as zf:
                csv_filename = zf.namelist()[0]
                for _, website in csv.reader(zf.open(csv_filename)):
                    if "http://" + website not in cache:
                        urls.append("http://" + website)
                        if len(urls) == self.maxurls:
                            break
            return urls

