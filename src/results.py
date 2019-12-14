import os
import sys
import time

from download import downloadurl

"""
Scrape the results of downloaded webpages.
"""

# Extract each URL from the list of URLs
urllist = [] # list of URLs from the input
for url in sys.argv[1]:
    urlllist.append(url.replace("\n", ""))

# Move up a directory to get to the "scrape" directory.
while os.getcwd().split("\")[-1] != "scrape":
    os.chdir("..") # Move up one directory.

numiter = 1000 # number of iterations (times) to test each scraper

for url in urllist:
    html = downloadurl(url)
    for line in html:
        with open("
