def register_scala_repl_tool(version, with_jline=False):...
classpath = [cls._create_compiler_jardep(version)]
if with_jline:
jline_dep = JarDependency(org='org.scala-lang', name='jline', rev=
    scala_build_info[version].full_version)
cls.register_jvm_tool(register, cls._key_for_tool_version('scala-repl',
    version), classpath=classpath)
classpath.append(jline_dep)
