# -*- coding: utf-8 -*-

import sys
import json
import pprint

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
        page_id = sys.argv[1]
    except IndexError:
        page_id = "PacktPub"
    pprint.pprint(graph(pageid))
