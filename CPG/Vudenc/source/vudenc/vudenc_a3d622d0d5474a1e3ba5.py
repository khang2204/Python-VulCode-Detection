from __future__ import absolute_import, division, print_function, unicode_literals
import os
import sys
from builtins import filter, object
from collections import defaultdict
from contextlib import contextmanager
from twitter.common.collections import OrderedSet
from pants.base.build_environment import get_buildroot, get_scm
from pants.base.worker_pool import SubprocPool
from pants.base.workunit import WorkUnit, WorkUnitLabel
from pants.build_graph.target import Target
from pants.engine.isolated_process import FallibleExecuteProcessResult
from pants.goal.products import Products
from pants.goal.workspace import ScmWorkspace
from pants.process.lock import OwnerPrintingInterProcessFileLock
from pants.reporting.report import Report
from pants.source.source_root import SourceRootConfig
"""Contains the context for a single run of pants.

  Task implementations can access configuration data from pants.ini and any flags they have exposed
  here as well as information about the targets involved in the run.

  Advanced uses of the context include adding new targets to it for upstream or downstream goals to
  operate on and mapping of products a goal creates to the targets the products are associated with.

  :API: public
  """
"""A logger facade that logs into the pants reporting framework."""
def __init__(self, run_tracker):...
self._run_tracker = run_tracker
def debug(self, *msg_elements):...
self._run_tracker.log(Report.DEBUG, *msg_elements)
def info(self, *msg_elements):...
self._run_tracker.log(Report.INFO, *msg_elements)
def warn(self, *msg_elements):...
self._run_tracker.log(Report.WARN, *msg_elements)
def error(self, *msg_elements):...
self._run_tracker.log(Report.ERROR, *msg_elements)
def fatal(self, *msg_elements):...
self._run_tracker.log(Report.FATAL, *msg_elements)
def __init__(self, options, run_tracker, target_roots, requested_goals=None,...
self._options = options
self.build_graph = build_graph
self.build_file_parser = build_file_parser
self.address_mapper = address_mapper
self.run_tracker = run_tracker
self._log = self.Log(run_tracker)
self._target_base = target_base or Target
self._products = Products()
self._buildroot = get_buildroot()
self._source_roots = SourceRootConfig.global_instance().get_source_roots()
self._lock = OwnerPrintingInterProcessFileLock(os.path.join(self._buildroot,
    '.pants.workdir.file_lock'))
self._java_sysprops = None
self.requested_goals = requested_goals or []
self._console_outstream = console_outstream or sys.stdout
self._scm = scm or get_scm()
self._workspace = workspace or (ScmWorkspace(self._scm) if self._scm else None)
self._replace_targets(target_roots)
self._invalidation_report = invalidation_report
self._scheduler = scheduler
@property...
"""docstring"""
return self._options
