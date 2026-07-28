from __future__ import absolute_import, division, print_function, unicode_literals
import os
import sys
from builtins import str
from future.utils import text_type
from pants.backend.python.rules.inject_init import InjectedInitDigest
from pants.backend.python.subsystems.pytest import PyTest
from pants.backend.python.subsystems.python_setup import PythonSetup
from pants.engine.fs import Digest, DirectoriesToMerge, DirectoryWithPrefixToStrip, Snapshot, UrlToFetch
from pants.engine.isolated_process import ExecuteProcessRequest, ExecuteProcessResult, FallibleExecuteProcessResult
from pants.engine.legacy.graph import BuildFileAddresses, TransitiveHydratedTargets
from pants.engine.legacy.structs import PythonTestsAdaptor
from pants.engine.rules import UnionRule, optionable_rule, rule
from pants.engine.selectors import Get
from pants.rules.core.core_test_model import Status, TestResult, TestTarget
from pants.source.source_root import SourceRootConfig
def parse_interpreter_constraints(python_setup, python_target_adaptors):...
constraints = {constraint for target_adaptor in python_target_adaptors for
    constraint in python_setup.compatibility_or_constraints(getattr(
    target_adaptor, 'compatibility', None))}
constraints_args = []
for constraint in sorted(constraints):
constraints_args.extend(['--interpreter-constraint', text_type(constraint)])
return constraints_args
