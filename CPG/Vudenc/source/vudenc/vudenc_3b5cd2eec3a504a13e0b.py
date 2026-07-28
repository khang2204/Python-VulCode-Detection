@memoized_method...
"""docstring"""
java_options_src = Java.global_instance()
scala_options_src = ScalaPlatform.global_instance()
def cp(instance, toolname):...
scope = instance.options_scope
return instance.tool_classpath_from_products(self._products, toolname,
    scope=scope)
