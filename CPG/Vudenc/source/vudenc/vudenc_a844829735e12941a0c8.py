@cached_property...
"""docstring"""
return [f for f in self.fields if hasattr(f, 'of') and issubclass(f.of,
    Resource)]
