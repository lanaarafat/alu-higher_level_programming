#!/usr/bin/python3
''' takes in URL,email,sends post request...'''
from urllib import parse, request
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascil')
    req = request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf.8'))
