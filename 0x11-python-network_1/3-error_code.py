#!/usr/bin/python3
"""
    a python script that takes and sends a request to the URL handling error, after taking the URL
"""


from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except error.HTTPError as exception:
        print("Error code: {}".format(exception.code))
