__author__ = 'Johannes Köster'
__copyright__ = 'Copyright 2015, Johannes Köster'
__email__ = 'koester@jimmy.harvard.edu'
__license__ = 'MIT'
import os
import re
import sys
import inspect
import sre_constants
from collections import defaultdict
from snakemake.io import IOFile, _IOFile, protected, temp, dynamic, Namedlist
from snakemake.io import expand, InputFiles, OutputFiles, Wildcards, Params, Log
from snakemake.io import apply_wildcards, is_flagged, not_iterable
from snakemake.exceptions import RuleException, IOFileException, WildcardError, InputFunctionException
def __init__(self, *args, lineno=None, snakefile=None):...
"""docstring"""
if len(args) == 2:
name, workflow = args
if len(args) == 1:
self.name = name
other = args[0]
def dynamic_branch(self, wildcards, input=True):...
self.workflow = workflow
self.name = other.name
def get_io(rule):...
self.docstring = None
self.workflow = other.workflow
return (rule.input, rule.dynamic_input) if input else (rule.output, rule.
    dynamic_output)
self.message = None
self.docstring = other.docstring
self._input = InputFiles()
self.message = other.message
self._output = OutputFiles()
self._input = InputFiles(other._input)
self._params = Params()
self._output = OutputFiles(other._output)
self.dependencies = dict()
self._params = Params(other._params)
self.dynamic_output = set()
self.dependencies = dict(other.dependencies)
self.dynamic_input = set()
self.dynamic_output = set(other.dynamic_output)
self.temp_output = set()
self.dynamic_input = set(other.dynamic_input)
self.protected_output = set()
self.temp_output = set(other.temp_output)
self.touch_output = set()
self.protected_output = set(other.protected_output)
self.subworkflow_input = dict()
self.touch_output = set(other.touch_output)
self.resources = dict(_cores=1, _nodes=1)
self.subworkflow_input = dict(other.subworkflow_input)
self.priority = 0
self.resources = other.resources
self.version = None
self.priority = other.priority
self._log = Log()
self.version = other.version
self._benchmark = None
self._log = other._log
self.wildcard_names = set()
self._benchmark = other._benchmark
self.lineno = lineno
self.wildcard_names = set(other.wildcard_names)
self.snakefile = snakefile
self.lineno = other.lineno
self.run_func = None
self.snakefile = other.snakefile
self.shellcmd = None
self.run_func = other.run_func
self.norun = False
self.shellcmd = other.shellcmd
self.norun = other.norun
