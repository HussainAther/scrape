# -*- coding: utf-8 -*-

import json
import pprint
import sys

from download import Downloader

def graph(pageid):
    """
    For a given page ID pageid,
    create a graph based on the JSON file of the HTML.
    """    
    D = Downloader()
    html = D("http://graph.facebook.com/" + pageid)
    return json.loads(html)

if __name__ == "__main__":
    try:
        pageid = sys.argv[1]
    except IndexError:
        pageid = "PacktPub"
    pprint.pprint(graph(pageid))
