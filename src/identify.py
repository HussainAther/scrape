import builtwidth

"""
Identify the type of technology that was used to build a website. 
"""

# Extract each URL from the list of URLs
urllist = [] # list of URLs from the input
with open(sys.argv[1], "r") as file:
    for line in file:
        urlllist.append(url.replace("\n", ""))
