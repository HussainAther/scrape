import lxml.html
import re

from bs4 import BeautifulSoup

"""
Evaluate the trade-offs of the three scraping approaches
by comparing their relative efficiency using Firebug.
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
    for field 
