# Scrape Tools

* `alexacb.py` : Callback function for the top sites by Alexa rank.
    - Usage: `python alexacb.py`
    - Requirements: pymongo (with `pip install pymongo` or `sudo pip install pymongo). 

* `browserrender.py` : Render a dynamic webpage and execute the JavaScript.
    - Usage: `python browserrender.py`
    - Requirements: [lxml](https://anaconda.org/anaconda/lxml), [PySide](https://anaconda.org/anaconda/pyside).

* `bs4test.py` : Sample code to run Beautiful Soup, which lets you navigate webpages.
    - Usage: `python bs4.py`
    - Requirements: Beautiful Soup (with `pip install bs4` or `sudo pip install bs4`).

* `cache.py` : Create cache directories of what you want to download.
    - Uasge: `python cache.py`

* `callback.py` : Output the scraped data to a csv file.
    - Usage `python callback.py`

* `compare.py` : Compare the performance of each web scraper using a different function for each.
    - Requirements: Beautiful Soup, lxml.

* `download.py` : This script has ways to download infomration from scraped results.
    - Usage: `python download.py`

* `facebook.py` : Navigate to a logged-in page on Facebook.
    - Usage: `python username password url`
    - Example: `python shussainather@gmail.com mypassword someurl` 
    - Requirements: [selenium](https://anaconda.org/conda-forge/selenium)

* `facebookgraph.py` : Create a graph based on each Facebook page visited for a specific page ID. 
    - Usage: `python ID` 

* `google.py` : Perform a simple Google Search on a keyword.
    - Usage: `python google.py keyword`

* `identify.py` : This script identifies the basics of technology that a website uses for a given file with a list of URLs to analyze using the `builtwith` and `whois` packages.
    - Usage: `python identify.py urlfile`
    - Example; `python identify.py urllist.txt`
    - Requirements: [builtwith](https://anaconda.org/auto/python-builtwith), [whois](https://anaconda.org/auto/python-whois).

* `indeedScrape.py` : This script scrapes Indeed for data science job postings for a given list of keywords and list of locations.
    - Usage: `python indeedScrape.py -k keywordsfile -l locationfile -r radius -m pagelimit`
    - Example usage: `python indeedScrape.py -k ../../data/indeed/keywords.txt -l ../../data/indeed/cities.txt -r 5 -m 2`
    - Requirements: Beautiful Soup, [pandas](https://anaconda.org/anaconda/pandas), selenium.
    - Uses Beautiful Soup to clean the document to get the HTML we need and Selenium for launching and using the browser.
    - Before running the script, you must create and use a new environment in which we install the required packages. `indeedScrape.py` requires a new conda environment to deal with package consistencies. We use the files listed in `indeedrequirements.txt` in the new environment. To create a new conda environment, use `conda create --name indeed` to create an environment called "indeed." To activate the environment, use `conda activate indeed.` Then use `conda config --add channel conda-forge` then `conda config --add channel anaconda` to add the channels we need. Finally, use `conda install --file indeedrequirements.txt` to download the required packages of the `indeedScrape.py` file.

* `lxmltest.py` : Use the Lxml Python wrapper parsing library for parsing HTML.
    - Usage: `python lxmltest.py`
    - Requirements: lxml.

* `mongocache.py` : Use MongoDB to implement a cache system for scraping with the pymongo wrapper.
    - Usage: `python mongocache.py`
    - Requirements: pymongo. 

* `mongoqueue.py` : More MongoDB functionality for creating cache systems. This script lets you queue jobs.

* `regex.py` : Use regular expressions to search through the HTML of a webpage from a list of URLs and a specific classtag given.
    - Usage: `python regex.py urlfile classtag`
    - Example; `python regex.py urllist.txt w2p_fw`

* `results.py` : Scrape results from the web using an input file with a list of URLs to scrape.
    - Usage: `python results.py urlfile`
    - Example: `python results.py urllist.txt`
