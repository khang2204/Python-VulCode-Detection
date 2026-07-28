import requests
import json
import bs4
import re
import sys
from multiprocessing import Pool
from time import strftime
if sys.version_info < (3, 0):
"""
    Custom KijijiApi exception class
    """
def __init__(self, dump=None):...
self.dumpfilepath = ''
if dump:
self.dumpfilepath = 'kijiji_dump_{}.txt'.format(strftime('%Y%m%dT%H%M%S'))
def __str__(self):...
f.write(dump)
if self.dumpfilepath:
return 'See {} in current directory for latest dumpfile.'.format(self.
    dumpfilepath)
return ''
