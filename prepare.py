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
print("Preparing day {} of advent of code".format(day))

os.mkdir(str(day), 0o777)

shutil.copyfile('test.py', os.path.join(str(day), 'test.py'))
os.chmod(os.path.join(str(day), 'test.py'), 0o777)

shutil.copyfile('solution.py', os.path.join(str(day), 'solution.py'))
os.chmod(os.path.join(str(day), 'solution.py'), 0o777)

os.chdir(str(day))

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

soup = BeautifulSoup(description, 'html.parser')
for i, test in enumerate(soup.find_all('pre'), start=1):
    with open("test{}.txt".format(i), 'w') as f:
        f.write(test.get_text())
    with open("test{}".format(i), 'w') as f:
        f.write("#!/bin/bash\n./test.py test{}.txt".format(i))
    os.chmod("test{}".format(i), 0o777)

with open('test', 'w') as f:
    f.write('#!/bin/bash\npython3 solution.py input.txt')

os.chmod('test', 0o777)
