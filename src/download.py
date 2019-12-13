import urllib2

"""
Download a webpage.
"""

def downloadurl(url):
    """
    Pass a URL to download it and return the HTML.
    """
    return urllib2.urlopen(url).read()
