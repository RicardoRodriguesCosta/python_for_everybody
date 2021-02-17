import urllib.request, urllib.parse, urllib.error
import ssl
import json as js

url = input("Enter location: ")
#url  = "http://py4e-data.dr-chuck.net/comments_42.json"
print("Retrieving "+url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

jasondata = (urllib.request.urlopen(url, context=ctx)).read().decode() #get http and decode as json string
print("Retrieved " + str(len(jasondata)) + " characters")
data = js.loads(jasondata) #open it like open()
#print(js.dumps(data, indent=4)) #Let me see my data please!
numbers = [data["comments"][n]["count"] for n in range(len(data["comments"]))] #List comprehension
#print(numbers)

print("Count: " + str(sum(numbers)))
print("Sum: " + str(len(numbers)))
#AND BA-BA-BUE  its done.
