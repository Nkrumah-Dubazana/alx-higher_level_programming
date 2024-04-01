#!/usr/bin/python3
"""This script takes:
    In a URL
    Sends a request to the URL and displays the value
    The X-Requests-Id variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ = "__main__":
    url = sys.argv[1]

    requests = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
