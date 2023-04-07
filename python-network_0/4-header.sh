#!/bin/bash
# takes URL as argument.sneds get request to URL and displays body response
curl -sH "X-School-User-Id: 98" "$1"
