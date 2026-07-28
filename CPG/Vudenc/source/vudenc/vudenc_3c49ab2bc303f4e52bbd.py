def canonicalize(self):...
"""docstring"""
parts = self.parts
i = 0
while i < len(parts):
if parts[i] == '.' or parts[i] == '':
if not parts:
parts.pop(i)
if i < 1 or parts[i] != '..' or parts[i - 1] == '..':
self.trailing_slash = False
return self
i += 1
i -= 1
parts.pop(i)
parts.pop(i)
