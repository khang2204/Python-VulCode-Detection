from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement
import logging
import os
import subprocess
from collections import namedtuple
from pants.base.exceptions import TaskError
from pants.binaries.binary_util import BinaryUtil
from pants.fs.archive import TGZ
from pants.subsystem.subsystem import Subsystem
from pants.util.contextutil import temporary_dir
from pants.util.memo import memoized_property
logger = logging.getLogger(__name__)
"""Represents a self-bootstrapping Node distribution."""
options_scope = 'node-distribution'
@classmethod...
return BinaryUtil.Factory,
