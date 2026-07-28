def register_custom_tool(key):...
dummy_jardep = JarDependency('missing spec', ' //:{}'.format(key))
cls.register_jvm_tool(register, cls._key_for_tool_version(key, 'custom'),
    classpath=[dummy_jardep])
