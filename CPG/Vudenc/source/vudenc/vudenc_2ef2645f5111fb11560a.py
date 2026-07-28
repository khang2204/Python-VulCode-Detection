import os
import pickle
from bs4 import BeautifulSoup
import urllib3
import certifi
import re
import sys
import argparse as ap
flatten = lambda l: [item for sublist in l for item in sublist]
def getytlinks(link):...
pm = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
html_page = pm.request('GET', link)
soup = BeautifulSoup(html_page.data, 'lxml')
links = [a.get('href') for a in soup('a') if a.get('href')]
new_links = [x for x in links if re.match('^https://youtu\\.be', x)]
newer_links = [x for x in links if re.match(
    '^https://www\\.youtube\\.com/watch', x)]
for lk in newer_links:
videolabel = re.search('v=([^&?]*)', lk)[1]
return new_links, links
if videolabel is None:
print('Reddytt: skipping URL without video label:', lk)
new_links.append('https://www.youtube.com/watch?v=' + videolabel)
