def register_custom_units(self):...
"""docstring"""
for unit in (self.metadata('custom_units') or []):
ureg.define(unit)
