import urllib2

strURL = 'http://api.wipmania.com/'
f = urllib2.urlopen(urllib2.Request(strURL))
response = f.read()
outerIP = response.split("<br>")[0]
f.close()
print outerIP
