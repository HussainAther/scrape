from bs4 import BeautifulSoup

"""
Sample code to test out Beautiful Soup.
"""

# Fix some broken HTML with the Beautiful Soup parser.
# In this HTML string, there are missing attribute quotes
# and clsoing tags. It also needs the <html> and <body> tags 
# to form a complete HTML document. 
brokenhtml = "<ul class=country><li>Area<li>Population</ul>"

# Parse the HTML.
soup = BeautifulSoup(brokenhtml, "html.parser")

# Make it pretty. 
fixedhtml = soup.prettify()

# Print the results.
print(fixedhtml)


