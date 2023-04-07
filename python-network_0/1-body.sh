#!/bin/bash
# takes and sends request to URLand displays body of response
curl -sfL "$1" -X GET
