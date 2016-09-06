# The program will prompt for a URL
# read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data
# compute the sum of the numbers in the file

import urllib
import json

url = raw_input("Enter URL")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_270125.json"
urlData = urllib.urlopen(url).read()
js = json.loads(urlData)
sum = 0
for x in js["comments"]:
    sum += x["count"]
print sum
