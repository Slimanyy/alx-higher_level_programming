#!/bin/bash
# shows all HTTP methods the server will accept.
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
