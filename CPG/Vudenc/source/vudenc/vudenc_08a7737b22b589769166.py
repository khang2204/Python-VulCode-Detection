import collections
import os
import pytest
import tempfile
import unittest
import reframe as rfm
import reframe.core.runtime as rt
import reframe.frontend.dependency as dependency
import reframe.frontend.executors as executors
import reframe.frontend.executors.policies as policies
import reframe.utility.os_ext as os_ext
from reframe.core.exceptions import DependencyError, JobNotStartedError
from reframe.frontend.loader import RegressionCheckLoader
import unittests.fixtures as fixtures
from unittests.resources.checks.hellocheck import HelloTest
from unittests.resources.checks.frontend_checks import BadSetupCheck, BadSetupCheckEarly, KeyboardInterruptCheck, RetriesCheck, SleepCheck, SleepCheckPollFail, SleepCheckPollFailLate, SystemExitCheck
def setUp(self):...
self.loader = RegressionCheckLoader(['unittests/resources/checks'],
    ignore_conflicts=True)
self.runner = executors.Runner(policies.SerialExecutionPolicy())
self.checks = self.loader.load_all()
rt.runtime().resources.prefix = tempfile.mkdtemp(dir='unittests')
rt.runtime()._current_run = 0
def tearDown(self):...
os_ext.rmtree(rt.runtime().resources.prefix)
def runall(self, checks, *args, **kwargs):...
cases = executors.generate_testcases(checks, *args, **kwargs)
self.runner.runall(cases)
def _num_failures_stage(self, stage):...
stats = self.runner.stats
return len([t for t in stats.failures() if t.failed_stage == stage])
