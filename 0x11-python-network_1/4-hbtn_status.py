#!/usr/bin/python3
"""
    a pyscript that fetch intranet https://intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":
    request = requests.get("https://intranet.hbtn.io/status")
    content = request.text
    encoding = request.encoding

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
