#!/usr/bin/python3
# GETING PUBLIC IP FROM DYNDNS.ORG
import urllib.request
from re import findall
def extIp(site):
    ipMask = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    if site == 'dyndns':
        url = 'http://checkip.dyndns.org'
        regexp = '<body>Current IP Address: ('+ipMask+')</body>'
    if site == 'google':
        url = 'https://www.google.co.uk/search?q=check+ip'
        regexp = '<!--m--><div.*?><div><div class=.*?>('+ipMask+').*?Your public IP address</div></div></div><!--n--></div>'

    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'    
        }
    )
    try:
        # opener = urllib.request.urlopen(url,timeout=10)
        opener = urllib.request.urlopen(req,timeout=10)
    except urllib.error.URLError as e:
        print(e.reason)
    html = opener.read()

    ip = findall(regexp,str(html))[0]

    return ip

# GETING LOCAL IP FROM SYSTEM
import socket
def localIp():
    get = socket.gethostname()
    ip = socket.gethostbyname(get)
    
    return ip

# CLI ARGUMENTS
import argparse
import sys
def flags():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-l', '--local', help='show local ip', action='store_true')
    parser.add_argument('-p', '--public', help='show public ip', action='store_true')
    parser.add_argument('-g', '--google', help='use google to check ip, faster but may block ip', action='store_true')
    parser.add_argument('-v', '--verbose', help='Make output verbose', action='store_true')

    args = parser.parse_args()
    # if no args
    if len(sys.argv) < 2:
        parser.print_help()
        print('\nYour local IP:', localIp())
        print('Your public IP:', extIp())

    if args.local:
        if args.verbose:
            print('system => Your local IP:', localIp())
        else:
            print(localIp())

    if args.google:
        site = 'google'
        args.public = True
    else:
        site = 'dyndns'

    if args.public:
        if args.verbose:
            print(site, '=> Your public IP:', extIp(site))
        else:
            print(extIp(site))
flags()
