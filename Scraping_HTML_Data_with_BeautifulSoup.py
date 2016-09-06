#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the sum of the numbers in the file.

from BeautifulSoup import BeautifulSoup
import urllib

url = raw_input("Enter - ")
if(len(url) < 1):
    url = "http://python-data.dr-chuck.net/comments_270124.html"
sum = 0
httpstring = urllib.urlopen(url).read()
soup = BeautifulSoup(httpstring)
tags = soup('span')
for tag in tags:
    sum = sum + int(tag.contents[0])
print sum
