from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import object
from pants.backend.jvm.subsystems.dependency_context import DependencyContext
from pants.backend.jvm.subsystems.java import Java
from pants.backend.jvm.subsystems.jvm_tool_mixin import JvmToolMixin
from pants.backend.jvm.subsystems.scala_platform import ScalaPlatform
from pants.backend.jvm.subsystems.shader import Shader
from pants.backend.jvm.targets.scala_jar_dependency import ScalaJarDependency
from pants.backend.jvm.tasks.classpath_products import ClasspathEntry
from pants.backend.jvm.tasks.classpath_util import ClasspathUtil
from pants.base.build_environment import get_buildroot
from pants.engine.fs import PathGlobs, PathGlobsAndRoot
from pants.java.jar.jar_dependency import JarDependency
from pants.subsystem.subsystem import Subsystem
from pants.util.dirutil import fast_relpath
from pants.util.memo import memoized_method, memoized_property
"""Configuration for Pants' zinc wrapper tool."""
ZINC_COMPILE_MAIN = 'org.pantsbuild.zinc.compiler.Main'
ZINC_EXTRACT_MAIN = 'org.pantsbuild.zinc.extractor.Main'
DEFAULT_CONFS = ['default']
ZINC_COMPILER_TOOL_NAME = 'zinc'
ZINC_EXTRACTOR_TOOL_NAME = 'zinc-extractor'
options_scope = 'zinc'
@classmethod...
return super(Zinc.Factory, cls).subsystem_dependencies() + (DependencyContext,
    Java, ScalaPlatform)
