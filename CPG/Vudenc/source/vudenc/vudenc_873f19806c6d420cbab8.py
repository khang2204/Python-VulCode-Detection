def compile_classpath(self, classpath_product_key, target, extra_cp_entries...
"""docstring"""
return list(entry.path for entry in self.compile_classpath_entries(
    classpath_product_key, target, extra_cp_entries))
