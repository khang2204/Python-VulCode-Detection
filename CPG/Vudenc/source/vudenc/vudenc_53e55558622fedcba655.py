__author__ = 'Johannes Köster'
__copyright__ = 'Copyright 2015, Johannes Köster'
__email__ = 'koester@jimmy.harvard.edu'
__license__ = 'MIT'
import os
import sys
import base64
import json
from collections import defaultdict
from itertools import chain
from functools import partial
from operator import attrgetter
from snakemake.io import IOFile, Wildcards, Resources, _IOFile
from snakemake.utils import format, listfiles
from snakemake.exceptions import RuleException, ProtectedOutputException
from snakemake.exceptions import UnexpectedOutputException
from snakemake.logging import logger
def jobfiles(jobs, type):...
return chain(*map(attrgetter(type), jobs))
