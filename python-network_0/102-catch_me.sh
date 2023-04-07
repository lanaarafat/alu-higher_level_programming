#!/bin/bash
# request that responds with amessage
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin:HolbertonSchool" -d "user_id=98"
