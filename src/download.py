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
