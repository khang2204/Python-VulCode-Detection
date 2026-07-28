__author__ = 'Johannes Köster'
__copyright__ = 'Copyright 2015, Johannes Köster'
__email__ = 'koester@jimmy.harvard.edu'
__license__ = 'MIT'
import re
import os
import sys
import signal
import json
import urllib
from collections import OrderedDict
from itertools import filterfalse, chain
from functools import partial
from operator import attrgetter
from snakemake.logging import logger, format_resources, format_resource_names
from snakemake.rules import Rule, Ruleorder
from snakemake.exceptions import RuleException, CreateRuleException, UnknownRuleException, NoRulesException, print_exception, WorkflowError
from snakemake.shell import shell
from snakemake.dag import DAG
from snakemake.scheduler import JobScheduler
from snakemake.parser import parse
import snakemake.io
from snakemake.io import protected, temp, temporary, expand, dynamic, glob_wildcards, flag, not_iterable, touch
from snakemake.persistence import Persistence
from snakemake.utils import update_config
def __init__(self, snakefile=None, snakemakepath=None, jobscript=None,...
"""docstring"""
self._rules = OrderedDict()
self.first_rule = None
self._workdir = None
self.overwrite_workdir = overwrite_workdir
self.workdir_init = os.path.abspath(os.curdir)
self._ruleorder = Ruleorder()
self._localrules = set()
self.linemaps = dict()
self.rule_count = 0
self.basedir = os.path.dirname(snakefile)
self.snakefile = os.path.abspath(snakefile)
self.snakemakepath = snakemakepath
self.included = []
self.included_stack = []
self.jobscript = jobscript
self.persistence = None
self.global_resources = None
self.globals = globals()
self._subworkflows = dict()
self.overwrite_shellcmd = overwrite_shellcmd
self.overwrite_config = overwrite_config
self.overwrite_configfile = overwrite_configfile
self.config_args = config_args
self._onsuccess = lambda log: None
self._onerror = lambda log: None
self.debug = debug
config = dict()
config.update(self.overwrite_config)
rules = Rules()
@property...
return self._subworkflows.values()
