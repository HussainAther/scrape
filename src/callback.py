import csv
import re

"""
This callback class and function scrapes the country data
and saves it in a readable csv format. The callback lets you
handle multiple websites by using the function after certain events
(such as after the webpages of interest have been downloaded).

In this case, the callback will take a url and html parameters and return
a list of more URLs to crawl.
"""

# Move up a directory to get to the "scrape" directory.
while os.getcwd().split("\")[-1] != "scrape":
    os.chdir("..") # Move up one directory.

# Make the output directory if it isn't there already.
if not os.path.isdir("/output/countries"):
    os.mkdir("output/countries")

class ScrapeCallBack:
    """
    A class to add a scrape callback parameter
    """
    def __init__(self):
        """
        Initialize the writer and fields.
        """
        self.fields = ("area", "population", "iso", "country", "capital",
                       "continent', "tld", "currency_code", "currency_name",
                       "phone", "postal_code_format", "postal_code"regex",
                       "languages", "neighbours")
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        """
        Check if we need to call the function again.
        """
        # Use regex to search the url for "/view" 
        if re.search("/view/", url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect("table > tr#places_{}_row_row > td.w2p_fw".format(field))[0].text_content())
            self.writer.writerow(row)
