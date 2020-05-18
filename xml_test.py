import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

URL = 'http://py4e-data.dr-chuck.net/comments_227372.xml'
Data = urllib.request.urlopen(URL, context=CTX).read()
Tree = ET.fromstring(Data)
lst = Tree.findall('comments/comment')

Count = 0
Sum = 0
for item in lst:
  Sum = Sum + int(item.find('count').text)
  Count = Count + 1

print(Count, 'Entries!')
print('Sum:', Sum)
