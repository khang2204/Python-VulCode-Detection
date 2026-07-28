import hashlib
import inspect
import logging
import os
import re
import sys
import tempfile
import csv
import gzip
from datetime import datetime
from time import time
from io import StringIO
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles
import pandas
import sqlalchemy
import lore
from lore.util import timer
from lore.stores import query_cached
logger = logging.getLogger(__name__)
@compiles(DropTable, 'postgresql')...
return compiler.visit_drop_table(element) + ' CASCADE'
