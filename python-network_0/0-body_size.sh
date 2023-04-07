#!/bin/bash
# takes, and sends URL,and displays size of vody of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
