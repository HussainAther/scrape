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
        html = url
