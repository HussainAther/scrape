import re
import os

# Check import to make sure it works with the Python version
try:
    import urllib as ul
    import urllib.parse as ulp 
except ImportError:
    import urllib2 as ul
    from urlparse import urlparse as ulp

class DiskCache:
    """
    Map a URL to a filename that will be used to save the 
    downloaded URL to the disk cache.
    """
