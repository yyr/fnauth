#!/usr/bin/env python3
import requests
import re

USERNAME = "testuser"
PASSWORD = "testuser"

URLS = ["http://www.tropmet.res.in", "http://google.com"]

URL = URLS[0]

info = dict(username=USERNAME, password=PASSWORD)

reqobj = requests.get(URL)
url = str(reqobj.url)

if "fgtauth" in url:
        magic = re.search('http.*\?', url).group()
        magic = url.replace(magic, "")
        info["magic"] = magic
        r = requests.post(url, data=info)
