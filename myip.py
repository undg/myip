#!/usr/bin/python3
import urllib.request
from re import findall

url = 'http://checkip.dyndns.org'
regexp = '<body>Current IP Address: (.*?)</body>'

req = urllib.request.urlopen(url,timeout=9)
html = req.read()

ip = findall(regexp,str(html))

print(ip[0])
