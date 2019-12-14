# -*- coding: utf-8 -*-

import urllib
import urlparse
import lxml.html
import sys

from download import Downloader

try:
    import urllib as ul
    import urllib.parse as ulp 
except ImportError:
    import urllib2 as ul
    from urlparse import urlparse as ulp

def search(keyword):
    """
    Google search for a keyword.
    """
    D = Downloader()
    url = 'https://www.google.com/search?q=' + urllib.quote_plus(keyword)
    html = D(url)
    tree = lxml.html.fromstring(html)
    links = []
    for result in tree.cssselect('h3.r a'):
        link = result.get('href')
        qs = urlparse.urlparse(link).query
        links.extend(urlparse.parse_qs(qs).get('q', []))
    return links

    
if __name__ == '__main__':
    try:
        keyword = sys.argv[1]
    except IndexError:
        keyword = 'test'
    print search(keyword)

