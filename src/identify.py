import builtwidth

"""
Identify the type of technology that was used to build a website. 
"""

# Extract each URL from the list of URLs
urllist = [] # list of URLs from the input
for url in sys.argv[1]:
    urlllist.append(url.replace("\n", ""))
