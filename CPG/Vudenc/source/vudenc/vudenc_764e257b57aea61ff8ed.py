from __future__ import absolute_import, division, print_function, unicode_literals
from collections import namedtuple
from pants.backend.jvm.subsystems.jvm_tool_mixin import JvmToolMixin
from pants.backend.jvm.subsystems.zinc_language_mixin import ZincLanguageMixin
from pants.backend.jvm.targets.jar_library import JarLibrary
from pants.build_graph.address import Address
from pants.build_graph.injectables_mixin import InjectablesMixin
from pants.java.jar.jar_dependency import JarDependency
from pants.subsystem.subsystem import Subsystem
major_version_info = namedtuple('major_version_info', ['full_version'])
scala_build_info = {'2.10': major_version_info(full_version='2.10.6'),
    '2.11': major_version_info(full_version='2.11.12'), '2.12':
    major_version_info(full_version='2.12.4')}
scala_style_jar = JarDependency('org.scalastyle', 'scalastyle_2.11', '0.8.0')
"""A scala platform.

  :API: public
  """
options_scope = 'scala'
@classmethod...
return JarDependency(org='org.scala-lang', name=name, rev=scala_build_info[
    version].full_version)
