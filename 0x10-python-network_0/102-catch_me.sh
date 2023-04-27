#!/bin/bash
curl -s -X POST -d "user_id=42" "0.0.0.0:5000/catch_me"
echo "The server has been caught!"
