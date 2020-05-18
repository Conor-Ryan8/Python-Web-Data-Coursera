import urllib.request, urllib.parse, urllib.error
import json
import ssl

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

URL = 'http://py4e-data.dr-chuck.net/comments_227373.json'
Data = urllib.request.urlopen(URL, context=CTX).read()
Dict = json.loads(Data)
print('User Count:',len(Dict['comments']))

Sum = 0
for Item in Dict['comments']:
  Sum = Sum + Item['count']

print('Sum:',Sum)
