#!/usr/local/bin/python3

from bs4 import BeautifulSoup
import urllib.request
import os
import requests
import shutil
import ssl
import stat
import subprocess
import sys

ssl._create_default_https_context = ssl._create_unverified_context

day = int(sys.argv[1])
if len(sys.argv) > 2:
    year = int(sys.argv[2])
else:
    year = 2020

print("Preparing day {} of advent of code {}".format(day, year))

day = '{:02d}'.format(day)

os.mkdir(day, 0o777)

shutil.copyfile('solution.py', os.path.join(day, 'solution.py'))
os.chmod(os.path.join(day, 'solution.py'), 0o777)

os.chdir(str(day))

url = "https://www.adventofcode.com/{}/day/{}".format(year, int(day))

cookie_str = "_ga=GA1.2.1513356176.1606798608; _gid=GA1.2.526309279.1607617280"
cookies = {}
for cookie in cookie_str.split(';'):
    cookie = cookie.strip()
    k, v = cookie.split('=')
    cookies[k] = v

def download(url):
    print("Downloading contents of: {}".format(url))
    return requests.get(url, cookies=cookies).text

description = download(url)

with open('test', 'w') as f:
    f.write('#!/bin/bash\npython3 -m unittest solution')

with open('run', 'w') as f:
    f.write('#!/bin/bash\nINPUT=${1:-input.txt}\ncat ${INPUT} | python3 solution.py')

os.chmod('solution.py', 0o666)
os.chmod('test', 0o777)
os.chmod('run', 0o777)
