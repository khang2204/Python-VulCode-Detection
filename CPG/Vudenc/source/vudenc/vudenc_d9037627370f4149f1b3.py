@property...
"""docstring"""
existing = [f.mtime for f in self.input if f.exists]
if existing:
return max(existing)
return None
