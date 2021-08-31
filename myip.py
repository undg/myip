#!/usr/bin/python3

def extIp(site): # GETING PUBLIC IP
    import urllib.request
    from re import findall

    ipMask = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    if site == 'dyndns':
        url = 'http://checkip.dyndns.org'
        regexp = '<body>Current IP Address: ('+ipMask+')</body>'
    if site == 'ipify':
        url = 'https://api.ipify.org/'
        regexp = '('+ipMask+')'
    req = urllib.request.Request( url, data=None, headers={
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

def localIp(): # GETING LOCAL IP FROM SYSTEM
    import socket
    get = socket.gethostname()
    ip = socket.gethostbyname(get)
    return ip

def flags(): # CLI ARGUMENTS
    import argparse
    import sys
    parser = argparse.ArgumentParser()

    # FLAGS
    parser.add_argument('-l', '--local', help='show local ip', action='store_true')
    parser.add_argument('-p', '--public', help='show public ip', action='store_true')
    parser.add_argument('-d', '--dyndns', help='use dyndns to check ip', action='store_true')
    parser.add_argument('-i', '--ipify', help='use ipify to check ip', action='store_true')
    parser.add_argument('-v', '--verbose', help='Make output verbose', action='store_true')

    args = parser.parse_args()
    # LOCAL IP
    if args.local:
        if args.verbose:
            print('system => Your local IP:', localIp())
        else:
            print(localIp())

    # PUBLIC IP
    if args.dyndns:
        site = 'dyndns'
        args.public = True
    if args.ipify:
        site = 'ipify'
        args.public = True
    else:
        site = 'ipify'

    if args.public:
        if args.verbose:
            print(site, '=> Your public IP:', extIp(site))
        else:
            print(extIp(site))

    # IF NO ARGS
    if len(sys.argv) < 2:
        parser.print_help()
        print('\nsystem => Your local IP:', localIp())
        print(site, '=> Your public IP:', extIp(site))

flags()
