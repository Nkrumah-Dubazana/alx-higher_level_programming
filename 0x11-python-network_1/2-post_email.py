#!/usr/bin/python3
"""Script that:
    Takes in a URL
    Sends a POST request to passed URL
    Takes email as a parameter
    Displays the body of the response
"""
import sys
import urllib.parse
import urllib.request

if __name__ = "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
