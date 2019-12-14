import csv

"""
This callback class and function scrapes the country data
and saves it in a readable csv format.
"""

# Move up a directory to get to the "scrape" directory.
while os.getcwd().split("\")[-1] != "scrape":
    os.chdir("..") # Move up one directory.
