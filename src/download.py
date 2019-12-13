import re
import urllib2

"""
Download a webpage.
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
      
def crawllink(seedurl, linkregex):
    """
    Crawl from the given seed URL seedurl following links
    matched by linkregex.
    """ 
