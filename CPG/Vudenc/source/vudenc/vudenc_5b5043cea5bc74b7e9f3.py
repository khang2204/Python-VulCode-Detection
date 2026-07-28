from time import sleep
import operator
from bs4 import BeautifulSoup
from requests import get
import constants
import logger
import re
import os
import pickle
import pysmash
from get_results import get_coalesced_tag
import datetime
DEFAULT_BASE_URLS = ['https://challonge.com/NP9ATX###',
    'http://challonge.com/heatwave###',
    'https://austinsmash4.challonge.com/atx###', 'http://challonge.com/RAA_###'
    ]
debug = False
LOG = logger.logger(__name__)
def _get_first_valid_url(base_url):...
valid = False
index = 1
while not valid:
url = base_url.replace('###', str(index))
return index
data, status = hit_url(url)
if status < 300 and is_valid(data, url=base_url):
if debug:
if debug:
print('url ' + url + ' is valid')
valid = True
print('url ' + url + ' is not valid')
index = index + 1
