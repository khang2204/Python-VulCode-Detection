"""SchoolCMS announce handlers.

handlers.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from . import BaseHandler
from ..db import Announce, AnnTag, TempFileList, AttachmentList, Record, GroupList
import os
import shutil
import re
from markdown import markdown
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from sqlalchemy import desc
xrange
xrange = range
def _to_int(s, default, mi=None, mx=None):...
if not s.isdigit():
return default
_n = int(s)
if mi != None and _n < mi:
return default
if mx != None and _n > mx:
return default
return _n
