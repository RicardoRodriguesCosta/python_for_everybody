import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('span')
#soma = 0
#count = 0
#for tag in tags:
#    soma = soma + int(tag.string)
#    count = count +1
#print("Count ", count)
#print("Sum ",soma)
print(soup)
