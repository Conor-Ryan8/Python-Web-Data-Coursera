import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
service = 'http://py4e-data.dr-chuck.net/json?'

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

address = 'Indian Institute of Technology Kharagpur India'
parms = dict()
parms['address'] = address
parms['key'] = api_key
url = service + urllib.parse.urlencode(parms)

handle = urllib.request.urlopen(url)
data = handle.read().decode()

js = json.loads(data)
location = js['results'][0]['place_id']
print(location)
