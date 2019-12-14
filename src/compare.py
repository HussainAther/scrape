import re

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
