from __future__ import absolute_import, division, print_function, unicode_literals
import errno
import logging
import os
import re
import textwrap
from builtins import open
from collections import defaultdict
from contextlib import closing
from hashlib import sha1
from xml.etree import ElementTree
from future.utils import PY3, text_type
from pants.backend.jvm.subsystems.java import Java
from pants.backend.jvm.subsystems.jvm_platform import JvmPlatform
from pants.backend.jvm.subsystems.scala_platform import ScalaPlatform
from pants.backend.jvm.subsystems.zinc import Zinc
from pants.backend.jvm.targets.annotation_processor import AnnotationProcessor
from pants.backend.jvm.targets.javac_plugin import JavacPlugin
from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.backend.jvm.targets.scalac_plugin import ScalacPlugin
from pants.backend.jvm.tasks.classpath_util import ClasspathUtil
from pants.backend.jvm.tasks.jvm_compile.jvm_compile import JvmCompile
from pants.base.build_environment import get_buildroot
from pants.base.exceptions import TaskError
from pants.base.hash_utils import hash_file
from pants.base.workunit import WorkUnitLabel
from pants.engine.fs import DirectoryToMaterialize, PathGlobs, PathGlobsAndRoot
from pants.engine.isolated_process import ExecuteProcessRequest
from pants.java.distribution.distribution import DistributionLocator
from pants.util.contextutil import open_zip
from pants.util.dirutil import fast_relpath, safe_open
from pants.util.memo import memoized_method, memoized_property
_SCALAC_PLUGIN_INFO_FILE = 'scalac-plugin.xml'
_JAVAC_PLUGIN_INFO_FILE = 'META-INF/services/com.sun.source.util.Plugin'
_PROCESSOR_INFO_FILE = (
    'META-INF/services/javax.annotation.processing.Processor')
logger = logging.getLogger(__name__)
"""An abstract base class for zinc compilation tasks."""
_name = 'zinc'
@staticmethod...
scalac_plugin_info_file = os.path.join(resources_dir, _SCALAC_PLUGIN_INFO_FILE)
f.write(textwrap.dedent(
    """
        <plugin>
          <name>{}</name>
          <classname>{}</classname>
        </plugin>
      """
    .format(scalac_plugin_target.plugin, scalac_plugin_target.classname)).
    strip())
@staticmethod...
javac_plugin_info_file = os.path.join(resources_dir, _JAVAC_PLUGIN_INFO_FILE)
classname = (javac_plugin_target.classname if PY3 else javac_plugin_target.
    classname.decode('utf-8'))
f.write(classname)
@staticmethod...
"""docstring"""
valid_patterns = {re.compile(p): v for p, v in whitelisted_args.items()}
def validate(idx):...
arg = args[idx]
for pattern, has_argument in valid_patterns.items():
if pattern.match(arg):
log.warn(
    "Zinc argument '{}' is not supported, and is subject to change/removal!"
    .format(arg))
return 2 if has_argument else 1
return 1
