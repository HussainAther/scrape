import sys
import time

from download import downloadurl

"""
Scrape the results of downloaded webpages.
"""

numiter = 1000 # number of iterations (times) to test each scraper
html = downloadurl(sys.argv[1])
