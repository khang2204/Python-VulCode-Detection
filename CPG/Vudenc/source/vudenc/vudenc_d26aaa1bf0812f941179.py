import logging
import re
import time
from six.moves import queue, range
from clickhouse_driver import Client, errors
from snuba import settings
logger = logging.getLogger('snuba.clickhouse')
ESCAPE_RE = re.compile('^-?[a-zA-Z][a-zA-Z0-9_\\.]*$')
NEGATE_RE = re.compile('^(-?)(.*)$')
def escape_col(col):...
if not col:
return col
if ESCAPE_RE.match(col):
return col
return u'{}`{}`'.format(*NEGATE_RE.match(col).groups())
