import lxml.html

"""
Parse some broken HTML text with lxml.
"""

# Broken HTMl
brokenhtml = "<ul class=country><li>Area<li>Population</ul>"

# Build an lxml tree to parse the HTML.
tree = lxml.html.fromtstring(brokenhtml)
 

