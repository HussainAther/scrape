import time
import lxml.html
import re

from bs4 import BeautifulSoup
from download import downloadurl

"""
Evaluate the trade-offs of the three scraping approaches
by comparing their relative efficiency using Firebug.

First, implement each scraper with one function for each.
"""

fields = ("area", "population", "iso", "country", "capital",
          "continent", "tld", "currency_code", "currency_name",
          "phone", "postal_code_format", "postal_code_regex", 
          "languages", "neighbours")

def rescraper(html):
    """
    Use regex to scrape.
    """
    results = {}
    for field in fields:
        # For each field, search the HTML using the following regex,
        # and add each finding to the results dictionary.
        results[field] = re.search('<td id="places_%s_row">.*?<td class="w2p_fw">(.*?)</td>' % field, html).groups()[0]
    return results

def bsscraper(html):
    """
    Use BeautifulSoup to clean the HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    results = {}
    for field in fields:
        # Same as with rescraper, but using the Beautiful Soup method.
        results[field] = soup.find("table").find("tr", id="places_%s_row" % field).find("td", class_="w2p_fw").text
    return results

def lxmlscraper(html):
    """
    lxml, mutatis mutandis.
    """
    tree = lxml.html.fromstring(html)
    results = {}
    for field in fields:
        results[field] = tree.cssselect("table > tr#plcaes_%s_row > td.w2p_fw" % field)[0].text_content()
    return results 

"""
Now, iterate through HTML for each scraper.
"""

numiter = 1000 # number of times to test (iterate through) each scraper

# Download the HTML for UK.
html = downloadurl("http://example.webscraping.com/places/default/view/United-Kingdom-239")

for name, scraper in [("regex", rescraper), 
                      ("BeautifulSoup", bsscraper),
                      ("lxml", lxmlscraper)]
    start = time.time() # Record the start time.
    for i in range(numiter):
        if scraper == rescraper:
            re.purge()
        result = scraper(html)
        # Check the scraped result.
        assert(result["area"] == "244,820 square kilometres") 
    # Record the end time.
    end = time.time()
    # Print how long it took.
    print("%s: %.2f seconds" % (name, end-start)) 
