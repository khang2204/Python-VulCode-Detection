def _tool_classpath(self, tool, products):...
"""docstring"""
return self.tool_classpath_from_products(products, self.
    _key_for_tool_version(tool, self.version), scope=self.options_scope)
