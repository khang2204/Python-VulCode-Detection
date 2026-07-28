from __future__ import unicode_literals
import collections
import datetime
import hashlib
import itertools
import os.path
import re
import time
from . import commands, helper, sheet, student, sendmail
Submission = collections.namedtuple('Submission', ['id', 'sheet_id',
    'student_id', 'time', 'files_path', 'deleted'])
def _match_subject(subject):...
return re.match('^Abgabe\\s*(?P<id>[0-9]+)', subject)
