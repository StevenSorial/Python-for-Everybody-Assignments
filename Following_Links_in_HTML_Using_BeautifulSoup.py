# The program will use urllib to read the HTML from the data files below,
# Extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list,
# Follow that link and repeat the process a number of times and report the last name you find.

from BeautifulSoup import BeautifulSoup
import urllib

url = raw_input("Enter Url: ")
if(len(url) < 1):
    url = "http://python-data.dr-chuck.net/known_by_Alannah.html"

count = raw_input("Enter Count: ")
if(len(count) < 1):
    count = 7
count = int(count)

position = raw_input("Enter Position: ")
if(len(position) < 1):
    position = 18
position = int(position)

while count > 0:
    httpstring = urllib.urlopen(url).read()
    print "Retrieving:", url
    soup = BeautifulSoup(httpstring)
    tags = soup('a')
    tag = tags[position - 1]
    url = tag.get("href", None)
    count -= 1
print tag.contents[0]
