from __future__ import absolute_import, division, print_function, unicode_literals
import itertools
import logging
import os
import pkgutil
import plistlib
from abc import abstractproperty
from builtins import object, open, str
from collections import namedtuple
from contextlib import contextmanager
from future.utils import PY3
from six import string_types
from pants.base.revision import Revision
from pants.java.util import execute_java, execute_java_async
from pants.subsystem.subsystem import Subsystem
from pants.util.contextutil import temporary_dir
from pants.util.memo import memoized_method, memoized_property
from pants.util.meta import AbstractClass
from pants.util.osutil import OS_ALIASES, normalize_os_name
from pants.util.process_handler import subprocess
logger = logging.getLogger(__name__)
def _parse_java_version(name, version):...
if isinstance(version, string_types):
version = Revision.lenient(version)
if version and not isinstance(version, Revision):
return version
