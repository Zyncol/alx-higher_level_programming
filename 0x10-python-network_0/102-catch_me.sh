#!/bin/bash
# Makes a request to 0.0.0.0:5000/
curl -sL -X PUT -H "Origin: You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
