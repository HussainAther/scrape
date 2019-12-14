import builtwith
import robotparser
import whois

# In Python 3, robotparser is part of urllib.
# In Python 2, it is its own module. Try to check
# which one works.
try:
    from urllib.robotparser import robotparser as rp
except ImportError:
    import robotparser as rp

"""
Identify the type of technology that was used to build a website, check who owns a 
website, and check for restrictions.
"""

# Extract each URL from the list of URLs
urllist = [] # list of URLs from the input
with open(sys.argv[1], "r") as file:
    for line in file:
        urlllist.append(url.replace("\n", ""))

# Initialize robotparser.
rp = robotparser.RobotFileParser()
agentname = "Crawler" 

# Parse each URL for the technology behind it.
# Builtwith should give info about the frameworks, programming languages,
# and servers used in building each website.
# WHOIS tells you who owns a website.
# Robotparser returns the robots.txt information about restrictions.
for url in urllist:
    builtwithparse(url)
    print.whois.whois(url)
    rp.set_url(url)
    rp.read()
