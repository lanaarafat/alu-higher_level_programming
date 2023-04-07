#!/usr/bin/python3
""" A python script that takes a URL, sends request and displays the value of variable found in the response header """
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[0]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
