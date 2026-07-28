from __future__ import absolute_import, division, print_function, unicode_literals
import os
from builtins import open
from future.utils import text_type
from pants.backend.graph_info.subsystems.cloc_binary import ClocBinary
from pants.base.workunit import WorkUnitLabel
from pants.engine.fs import FilesContent, PathGlobs, PathGlobsAndRoot
from pants.engine.isolated_process import ExecuteProcessRequest
from pants.task.console_task import ConsoleTask
from pants.util.contextutil import temporary_dir
"""Print counts of lines of code."""
@classmethod...
return super(CountLinesOfCode, cls).subsystem_dependencies() + (ClocBinary,)
