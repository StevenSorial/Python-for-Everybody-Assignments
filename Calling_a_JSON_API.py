# The program will prompt for a location,
# contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib
import json

loc = raw_input('Enter location: ')
if len(loc) < 1:
    loc = "Cranfield University"
Cranfield University
url = "http://maps.googleapis.com/maps/api/geocode/json?" + urllib.urlencode({'address': loc})
data = urllib.urlopen(url).read()
js = json.loads(data)

print js["results"][0]["place_id"]
