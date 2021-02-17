import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
tag = "a"
url = input('Enter URL: ')
"""Function that receive's an url, parse the data and spits out
a new url of the specified position"""
def url_to_url(url,tag,position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup(tag)
    list_urls = [tag.get("href",None) for tag in tags]
    #print(list_urls)
    url = list_urls[position]
    print("Retrieving: ", url)
    return url

check = 0
count = int(input("Enter count: "))
position = int(input("Enter position: "))
position = position -1
print("Retrieving: ", url)

while check < count:
    url = url_to_url(url,tag,position)
    #print("Retrieving: ", url)
    check = check +1
