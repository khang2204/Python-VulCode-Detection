@property...
"""docstring"""
return set(f for f in self.input if not f.exists and not f in self.
    subworkflow_input)
