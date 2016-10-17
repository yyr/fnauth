#!/usr/bin/env python3
import requests
import re

USERNAME = "testuser"
PASSWORD = "testuser"


debug = False
info = dict(username=USERNAME, password=PASSWORD)

URLS = ["http://www.tropmet.res.in", "http://google.com"]
for URL in URLS:
    reqobj = requests.get(URL)
    url = str(reqobj.url)

    if debug:
        print("requested: " + URL)

    # Start authentication.
    if "fgtauth" in url:
        magic = re.search('http.*\?', url).group()
        magic = url.replace(magic, "")
        info["magic"] = magic
        r = requests.post(url, data=info)
        # print(r.text)

    else:
        if debug:
            print("Seems already authenticated")
