from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import os
from builtins import str
from future.utils import text_type
from pants.backend.jvm import argfile
from pants.backend.jvm.subsystems.java import Java
from pants.backend.jvm.subsystems.jvm_platform import JvmPlatform
from pants.backend.jvm.targets.annotation_processor import AnnotationProcessor
from pants.backend.jvm.targets.javac_plugin import JavacPlugin
from pants.backend.jvm.targets.jvm_target import JvmTarget
from pants.backend.jvm.tasks.jvm_compile.jvm_compile import JvmCompile
from pants.base.exceptions import TaskError
from pants.base.workunit import WorkUnit, WorkUnitLabel
from pants.engine.fs import DirectoryToMaterialize
from pants.engine.isolated_process import ExecuteProcessRequest
from pants.java.distribution.distribution import DistributionLocator
from pants.util.dirutil import safe_open
from pants.util.process_handler import subprocess
_JAVAC_PLUGIN_INFO_FILE = 'META-INF/services/com.sun.source.util.Plugin'
_PROCESSOR_INFO_FILE = (
    'META-INF/services/javax.annotation.processing.Processor')
logger = logging.getLogger(__name__)
"""Compile Java code using Javac."""
_name = 'java'
@staticmethod...
javac_plugin_info_file = os.path.join(resources_dir, _JAVAC_PLUGIN_INFO_FILE)
f.write(javac_plugin_target.classname)
@classmethod...
return '-encoding', 'UTF-8'
