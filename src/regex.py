import re

from download import downloadurl 

"""
This script uses regular expressions to match the contents of a <td>
element in the HTML of a webpage.
"""

# Extract each URL from the list of URLs
urllist = [] # list of URLs from the input
with open(sys.argv[1], "r") as file:
    for line in file:
        urlllist.append(url.replace("\n", ""))

# Search through the HTML of each URL.
for url in urllist:
    html = downloadurl(url) # Extract the HTML.
    re.findall('<td class="2p_fw">(.*?)</td>, html)
