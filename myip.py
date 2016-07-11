#!/usr/bin/python3
# GETING EXTERNAL IP FROM DYNDNS.ORG
import urllib.request
from re import findall
def extIp():
    url = 'http://checkip.dyndns.org'
    regexp = '<body>Current IP Address: (.*?)</body>'

    try:
        opener = urllib.request.urlopen(url,timeout=10)
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
def options():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-l', '--local', help='show local ip', action='store_true')
    parser.add_argument('-e', '--external', help='show external ip', action='store_true')
    parser.add_argument('-v', '--verbose', help='Make output verbose', action='store_true')

    args = parser.parse_args()
    # if no args
    if len(sys.argv) < 2:
        parser.print_help()
        print('\nYour local IP:', localIp())
        print('Your external IP:', extIp())

    if args.local:
        if args.verbose:
            print('Your local IP:', localIp())
        else:
            print(localIp())
    if args.external:
        if args.verbose:
            print('Your external IP:', extIp())
        else:
            print(extIp())
options()
