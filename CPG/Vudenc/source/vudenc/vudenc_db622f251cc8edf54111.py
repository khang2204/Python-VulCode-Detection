"""
sabnzbd.database - Database Support
"""
import sqlite3
import os
import pysqlite2.dbapi2 as sqlite3
import time
import zlib
import logging
import sys
import threading
import sabnzbd
import sabnzbd.cfg
from sabnzbd.constants import DB_HISTORY_NAME, STAGES
from sabnzbd.encoding import unicoder
from sabnzbd.bpsmeter import this_week, this_month
from sabnzbd.decorators import synchronized
from sabnzbd.misc import get_all_passwords, int_conv
DB_LOCK = threading.RLock()
def convert_search(search):...
"""docstring"""
if not search:
search = ''
search = search.replace('*', '%').replace(' ', '%')
if search and search.startswith('^'):
search = search.replace('^', '')
if search and search.endswith('$'):
search += '%'
search = search.replace('$', '')
search = '%' + search + '%'
return search
search = '%' + search
