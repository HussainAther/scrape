import re
import urllib2
import urlparse

# In Python 3, robotparser is part of urllib.
# In Python 2, it is its own module. Try to check
# which one works.
try:
    from urllib.robotparser import robotparser as rp
except ImportError:
    import robotparser as rp

"""
This script contains functions and code to download a webpage.
"""

def downloadurl(url):
    """
    Pass a URL to download it and return the HTML.
    """
    print("Downloading:", url)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError:
        print("Download error:", urllib2.URLError.reason)
        html = None
    return html

def crawlsitemap(url):
    """
    Sitemap crawler
    """
    sitemap = downloadurl(url) # Download the sitemap file.
    links = re.findall("<loc>*.*?)</loc>", sitemap) # Extract the sitemap links.
    for link in links:
        html = downloadurl(link)
      
def crawllink(seedurl, linkregex, agentname, rp):
    """
    Crawl from the given seed URL seedurl following links
    matched by linkregex for an agentname of the crawler and
    initialized robot parser.
    """ 
    queue = [seedurl]
    while queue:
        url = queue.pop()
        html = downloadurl(url)
        if rp.can_fetch(agentname, url)
            for link in getlinks(htmls): # Filter for links matching regex.
                if re.match(linkregex, link):
                    queue.append(link)
        else:
            print("Blocked by robots.")

def getlinks(html):
    """
    Return a list of links from html.
    """
    # Regex to extract all links from a webpage.
    webpageregex = re.compile("<a[^>]+href=["\"]*.*?)["\"], re.IGNORECASE)
    # Return list of all links from the webpage.
    return webpageregex.findall(html) 

class Throttle:
    """
    Add a delay between downloads to the same domain.
    """
    def __init__(self, delay):
        self.delay = delay # amount of time delay between downloads to each domain
        self.domains = {} # timestamp when domain was last accessed
        
    def wait(self, url):
        """
        Wait for URL to load.
        """
        domain = urlparse.urlparse(url).netloc
        lastaccessed = self.domains.get(domain)
        if self.delay > 0 and lastaccessed is not None:
            sleepsecs = self.delay - (datetime.datetime.now() - lastaccessed).seconds
            if sleepsecs > 0: # domain accessed recently
                time.sleep(sleepsecs) # sleep for a bit
            self.domains[domain] = datetime.datetime.now() # Update the last accessed time.

