import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

Pos = input('Position: ')
Count = input('Counter: ')
URL = input('URL: ')

def getURL(URL):
  HTML = urllib.request.urlopen(URL, context=CTX).read()
  Soup = BeautifulSoup(HTML, "html.parser")
  Tag = Soup('a')
  return str(Tag[int(Pos)-1].get('href',None))

for i in range(0,int(Count)+1):
  print(URL)
  URL = getURL(URL)
