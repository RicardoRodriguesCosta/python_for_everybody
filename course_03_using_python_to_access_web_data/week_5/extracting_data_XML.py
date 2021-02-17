import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input("Enter location: ")
print("Retrieving "+url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

XML = urllib.request.urlopen(url, context=ctx) #get xml from the interwebs
data = XML.read() #open it like open()
print("Retrieved " + str(len(data)) + " characters") #tell how many characters in total
tree = ET.fromstring(data) #Transform into a xml.etree.ElementTree.Element
numbers = tree.findall('.//count') #find all count attrib in the tree and put them in a list
suma = 0
count = 0
for number in numbers: #read through the list (THINK HOW TO TRANSFORM THIS IN A LIST COMPREHENSION)
    suma = suma + int(number.text)
    count = count +1
names = tree.findall('.//name')

print("Count: " + str(count))
print("Sum: " + str(suma))
#AND BA-BA-BUE  its done.
