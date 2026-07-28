def to_dir(self):...
"""docstring"""
clone = self.clone()
if not clone.trailing_slash:
clone.parts.pop()
clone.trailing_slash = bool(clone.parts)
return clone
