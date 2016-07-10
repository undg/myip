#!/usr/bin/python

import urllib.request, re


url = 'http://checkip.dyndns.org'
regexp = '<body>Current IP Address: (.*?)</body>'

req = urllib.request.urlopen(url,timeout=3)
html = req.read()

ip = re.findall(regexp,str(html))

print(ip[0])
