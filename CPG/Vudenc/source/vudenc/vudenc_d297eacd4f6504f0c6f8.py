from flask import request
from clickhouse_driver.errors import Error as ClickHouseError
from datetime import date, datetime, timedelta
from dateutil.parser import parse as dateutil_parse
from dateutil.tz import tz
from functools import wraps
from hashlib import md5
from itertools import chain, groupby
import jsonschema
import logging
import numbers
import re
import simplejson as json
import six
import _strptime
import time
from snuba import clickhouse, schemas, settings, state
from snuba.clickhouse import escape_col, ALL_COLUMNS, PROMOTED_COLS, TAG_COLUMN_MAP, COLUMN_TAG_MAP
logger = logging.getLogger('snuba.util')
NESTED_COL_EXPR_RE = re.compile('^(tags|contexts)\\[([a-zA-Z0-9_\\.:-]+)\\]$')
PART_RE = re.compile("\\('(\\d{4}-\\d{2}-\\d{2})', (\\d+)\\)")
DATE_TYPE_RE = re.compile('(Nullable\\()?Date\\b')
DATETIME_TYPE_RE = re.compile('(Nullable\\()?DateTime\\b')
QUOTED_LITERAL_RE = re.compile("^'.*'$")
def __init__(self, literal):...
self.literal = literal
def to_list(value):...
return value if isinstance(value, list) else [value]
