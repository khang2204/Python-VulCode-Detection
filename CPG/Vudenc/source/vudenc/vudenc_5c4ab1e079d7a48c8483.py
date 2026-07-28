from __future__ import absolute_import, division, print_function, unicode_literals
import logging
from textwrap import dedent
from pants.backend.native.subsystems.native_toolchain import NativeToolchain
from pants.backend.native.targets.native_library import NativeLibrary
from pants.backend.python.python_requirement import PythonRequirement
from pants.backend.python.subsystems import pex_build_util
from pants.backend.python.subsystems.python_setup import PythonSetup
from pants.backend.python.targets.python_distribution import PythonDistribution
from pants.base.exceptions import IncompatiblePlatformsError
from pants.binaries.executable_pex_tool import ExecutablePexTool
from pants.subsystem.subsystem import Subsystem
from pants.util.memo import memoized_property
from pants.util.objects import SubclassesOf
logger = logging.getLogger(__name__)
"""A subsystem which exposes components of the native backend to the python backend."""
options_scope = 'python-native-code'
default_native_source_extensions = ['.c', '.cpp', '.cc']
@classmethod...
super(PythonNativeCode, cls).register_options(register)
register('--native-source-extensions', type=list, default=cls.
    default_native_source_extensions, fingerprint=True, advanced=True, help
    =
    'The extensions recognized for native source files in `python_dist()` sources.'
    )
@classmethod...
return super(PythonNativeCode, cls).subsystem_dependencies() + (NativeToolchain
    .scoped(cls), PythonSetup)
