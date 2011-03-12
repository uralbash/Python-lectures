#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup

strURL = 'http://www.viewmyipaddress.com/'
f = urllib2.urlopen(urllib2.Request(strURL))
soup = BeautifulSoup(f.read())
f.close()
outerIP = soup.find("p", {"id":"copytext"}).contents[0]
print outerIP
