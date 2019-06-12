# Indeed web scraping

* `indeedScrape.py` : This script scrapes Indeed for data science job postings for a given list of keywords and list of locations.
    - Usage: `python indeedScrape.py -k keywordsfile -l locationfile -r radius -m pagelimit`
    - Example usage: `python indeedScrape.py -k ../../data/indeed/keywords.txt -l ../../data/indeed/cities.txt -r 5 -m 2`
    - Requirements: Beautiful Soup (with `pip install bs4` or `sudo pip install bs4`), pandas, [selenium](https://anaconda.org/conda-forge/selenium).
    - Uses Beautiful Soup to clean the document to get the HTML we need and Selenium for launching and using the browser.
    - Before running the script, you must create and use a new environment in which we install the required packages. `indeedScrape.py` requires a new conda environment to deal with package consistencies. We use the files listed in `indeedrequirements.txt` in the new environment. To create a new conda environment, use `conda create --name indeed` to create an environment called "indeed." To activate the environment, use `conda activate indeed.` Then use `conda config --add channel conda-forge` then `conda config --add channel anaconda` to add the channels we need. Finally, use `conda install --file indeedrequirements.txt` to download the required packages of the `indeedScrape.py` file.

