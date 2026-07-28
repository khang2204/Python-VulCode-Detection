def __eq__(self, other):...
if isinstance(other, TraversalPath):
return hash(self) == hash(other)
return False
