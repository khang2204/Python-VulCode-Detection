@classmethod...
super(Zinc.Factory, cls).register_options(register)
zinc_rev = '1.0.3'
shader_rules = [Shader.exclude_package('scala', recursive=True), Shader.
    exclude_package('xsbt', recursive=True), Shader.exclude_package('xsbti',
    recursive=True), Shader.exclude_package('org.apache.logging.log4j',
    recursive=True)]
cls.register_jvm_tool(register, Zinc.ZINC_COMPILER_TOOL_NAME, classpath=[
    JarDependency('org.pantsbuild', 'zinc-compiler_2.11', '0.0.7')], main=
    Zinc.ZINC_COMPILE_MAIN, custom_rules=shader_rules)
cls.register_jvm_tool(register, 'compiler-bridge', classpath=[
    ScalaJarDependency(org='org.scala-sbt', name='compiler-bridge', rev=
    zinc_rev, classifier='sources', intransitive=True)])
cls.register_jvm_tool(register, 'compiler-interface', classpath=[
    JarDependency(org='org.scala-sbt', name='compiler-interface', rev=
    zinc_rev)], main='no.such.main.Main', custom_rules=shader_rules)
cls.register_jvm_tool(register, Zinc.ZINC_EXTRACTOR_TOOL_NAME, classpath=[
    JarDependency('org.pantsbuild', 'zinc-extractor_2.11', '0.0.4')])
