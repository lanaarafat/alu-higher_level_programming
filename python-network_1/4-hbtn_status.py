#!/usr/bin/python3
''' script fetches URL '''


import requests


if __name__ == "__main__":
    response =  requests.get('https://alu-intranet.hbtn.io/status')
    print ('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t),t))
