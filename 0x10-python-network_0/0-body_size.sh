#!/bin/bash
#shows/ displays the size of the content length body of the response
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
