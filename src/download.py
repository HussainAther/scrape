import random
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

# Same for urllib2
try:
    import urllib as ul
    import urllib.parse as ulp 
except ImportError:
    import urllib2 as ul
    from urlparse import urlparse as ulp

from callback import ScrapeCallBack

"""
This script contains functions and code to download a webpage.
"""

def downloadurl(url, useragent="wswp", proxy=None, retries=2):
    """
    Pass a URL to download it and return the HTML.
    You can also run this function with a specific useragent, proxy, and 
    different number of retries.
    """
    print("Downloading:", url)
    headers = {"User-agent": useragent} # Use the agent name as a header.
    request = ul.request(url, headers=headers) # Form the request.
    opener = ul.request.opener() 
    html = ul.request.urlopen(url).read()
    if proxy: # if we are using a proxy
        proxyparams = {ulp.urlparse(url).scheme:proxy} # Use the proxy.
        opener.add_handler(ul.ProxyHandler(proxyparams)
    try:
        html = opener.open(request).read()
    except:
        e = ul.URLError
        print("Download error;", ereason)
        html = None
        if retries > 0:
            if hasattr(e, "code") and 500 <= e.code < 600: # Check the error codes
                                                           # to make sure you can try again.
                html = downloadurl(url, useragent, proxy, retries-1) # Try again.
    return html

def crawlsitemap(url):
    """
    Sitemap crawler
    """
    sitemap = downloadurl(url) # Download the sitemap file.
    links = re.findall("<loc>*.*?)</loc>", sitemap) # Extract the sitemap links.
    for link in links:
        html = downloadurl(link)
    
def crawllink(seedurl, linkregex=None, delay=5, maxdepth=-1, maxurls=-1, useragent="wswp", proxies=None, retries=1, scallback=None, cache=None):
    """
    Crawl from the given seed URL seedurl following links
    matched by linkregex for an agentname of the crawler and
    initialized robot parser. You can add a maxdepth to determine
    how many pages you will crawl. You can also add a scrape
    callback scallback to search multiple websites.
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = [seedurl]
    # the URL's that have been seen and at what depth
    seen = {seedurl: 0}
    # track how many URL's have been downloaded
    num_urls = 0
    rp = get_robots(seedurl)
    D = Downloader(delay=delay, useragent=useragent, proxies=proxies, retries=retries, cache=cache)
    while crawl_queue:
        url = crawl_queue.pop()
        depth = seen[url]
        # check url passes robots.txt restrictions
        if rp.can_fetch(useragent, url):
            html = D(url)
            links = []
            if scallback:
                links.extend(scallback(url, html) or [])

            if depth != maxdepth:
                # can still crawl further
                if linkregex:
                    # filter for links matching our regular expression
                    links.extend(link for link in get_links(html) if re.match(linkregex, link))

                for link in links:
                    link = normalize(seedurl, link)
                    # check whether already crawled this link
                    if link not in seen:
                        seen[link] = depth + 1
                        # check link is within same domain
                        if same_domain(seedurl, link):
                            # success! add this new link to queue
                            crawl_queue.append(link)

            # check whether have reached downloaded maximum
            num_urls += 1
            if num_urls == maxurls:
                break
        else:
            print("Blocked by robots.txt:", url)

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
    You do this by "sleeping" between consecutive downloads.
    """
    def __init__(self, delay):
        self.delay = delay # amount of time delay between downloads to each domain
        self.domains = {} # timestamp when domain was last accessed
        
    def wait(self, url):
        """
        Wait for URL to load.
        """
        domain = urlparse.urlparse(url).netloc
        lastaccessed = self.domains.get(domain) # when the url was last accessed
        if self.delay > 0 and lastaccessed is not None: # if we have set a delay
            sleepsecs = self.delay - (datetime.datetime.now() - lastaccessed).seconds # calculate how long we sleep
            if sleepsecs > 0: # domain accessed recently
                time.sleep(sleepsecs) # sleep for a bit
            self.domains[domain] = datetime.datetime.now() # Update the last accessed time.

url = "http://example.webscraping.com/"
reparse = "/(index|view)"

# Perform the link crawl with the ScrapeCallBack to output the data to 
# a csv file.
crawllink(url, reparse, -1, ScrapeCallBack())

class Downloader:
    """
    Download while supporting cached files.
    """
    def __init__(self, delay=5, useragent="wswp", proxies=None, retries=1, cache=None):
        """
        Initialize the throttle delay while downloading.
        """
        self.throttle = Throttle(delay)
        self.useragent = useragent
        self.proxies = proxies
        self.retries = retries
        self.cache = cache
    
    def __call__(self, url):
        """
        Callback to check each URL.
        """
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError as e:
                pass # if there's no URL available in the cache
        else:
            if self.retries > 0 and 500 <= result["code"] < 600:
                # Server error means you can re-download.
                result = None
        if result is None:
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None
            headers = {"User-agent": self.useragent}
            result = self.downloadurl(url, headers, proxy, self.retries)
        if self.cache:
            self.cache[url] = result
        return result["html"]
 
    def download(self, url, headers, proxy, retries, data=None):
        """
        Download and cache.
        """
        print("Downloading:", url)
        request = ul.request(url, headers=headers) # Form the request.
        opener = ul.request.opener() 
        if proxy:
            proxyparams = {ulp.urlparse(url).scheme:proxy} # Use the proxy.
            opener.add_handler(ul.ProxyHandler(proxyparams)
        try:
            response = opener.open(request)
            html = response.read()
            code = response.code
        except Exception as e:
            print("Download error:", str(e))
            html = ""
            if hasattr(e, "code"):
                code = e.code
                if retries > 0 and 500 <= code < 600:
                    # retry 5XX HTTP errors
                    return self._get(url, headers, proxy, retries-1, data)
            else:
                code = None
        return {"html": html, "code": code}
