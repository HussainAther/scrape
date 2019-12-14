import builtwidth
import whois

"""
Identify the type of technology that was used to build a website. 
"""

# Extract each URL from the list of URLs
urllist = [] # list of URLs from the input
with open(sys.argv[1], "r") as file:
    for line in file:
        urlllist.append(url.replace("\n", ""))

# Parse each URL for the technology behind it.
# This should give info about the frameworks, programming languages,
# and servers used in building each website.
for url in urllist:
    builtwithparse(url)
    print.whois.whois(url)
