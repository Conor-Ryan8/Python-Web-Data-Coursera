import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

Test = 'http://py4e-data.dr-chuck.net/comments_42.html'
URL = 'http://py4e-data.dr-chuck.net/comments_227370.html'

HTML = urllib.request.urlopen(URL, context=CTX).read()
Soup = BeautifulSoup(HTML, "html.parser")
Sum = 0
Count = 0
Tags = Soup('span')
for Tag in Tags:
  Sum = Sum + int(Tag.contents[0])
  Count = Count + 1
print('Count:',Count)
print('Sum:',Sum)
