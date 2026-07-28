@classmethod...
def register_scala_compiler_tool(version):...
cls.register_jvm_tool(register, cls._key_for_tool_version('scalac', version
    ), classpath=[cls._create_compiler_jardep(version)])
def register_scala_repl_tool(version, with_jline=False):...
classpath = [cls._create_compiler_jardep(version)]
if with_jline:
jline_dep = JarDependency(org='org.scala-lang', name='jline', rev=
    scala_build_info[version].full_version)
cls.register_jvm_tool(register, cls._key_for_tool_version('scala-repl',
    version), classpath=classpath)
classpath.append(jline_dep)
def register_style_tool(version):...
cls.register_jvm_tool(register, cls._key_for_tool_version('scalastyle',
    version), classpath=[scala_style_jar])
super(ScalaPlatform, cls).register_options(register)
register('--scalac-plugins', advanced=True, type=list, fingerprint=True,
    help='Use these scalac plugins.')
register('--scalac-plugin-args', advanced=True, type=dict, default={},
    fingerprint=True, help=
    'Map from scalac plugin name to list of arguments for that plugin.')
cls.register_jvm_tool(register, 'scalac-plugin-dep', classpath=[], help=
    'Search for scalac plugins here, as well as in any explicit dependencies.')
register('--version', advanced=True, default='2.12', choices=['2.10',
    '2.11', '2.12', 'custom'], fingerprint=True, help=
    'The scala platform version. If --version=custom, the targets //:scala-library, //:scalac, //:scala-repl and //:scalastyle will be used, and must exist.  Otherwise, defaults for the specified version will be used.'
    )
register('--suffix-version', advanced=True, default=None, help=
    'Scala suffix to be used in `scala_jar` definitions. For example, specifying `2.11` or `2.12.0-RC1` would cause `scala_jar` lookups for artifacts with those suffixes.'
    )
register_scala_compiler_tool('2.10')
register_scala_repl_tool('2.10', with_jline=True)
register_style_tool('2.10')
register_scala_compiler_tool('2.11')
register_scala_repl_tool('2.11')
register_style_tool('2.11')
register_scala_compiler_tool('2.12')
register_scala_repl_tool('2.12')
register_style_tool('2.12')
def register_custom_tool(key):...
dummy_jardep = JarDependency('missing spec', ' //:{}'.format(key))
cls.register_jvm_tool(register, cls._key_for_tool_version(key, 'custom'),
    classpath=[dummy_jardep])
register_custom_tool('scalac')
register_custom_tool('scala-repl')
register_custom_tool('scalastyle')
