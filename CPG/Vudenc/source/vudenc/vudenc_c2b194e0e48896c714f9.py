__author__ = 'Johannes Köster'
__copyright__ = 'Copyright 2015, Johannes Köster'
__email__ = 'koester@jimmy.harvard.edu'
__license__ = 'MIT'
import os
import re
import stat
import time
import json
from itertools import product, chain
from collections import Iterable, namedtuple
from snakemake.exceptions import MissingOutputException, WorkflowError, WildcardError
from snakemake.logging import logger
def lstat(f):...
return os.stat(f, follow_symlinks=os.stat not in os.supports_follow_symlinks)
