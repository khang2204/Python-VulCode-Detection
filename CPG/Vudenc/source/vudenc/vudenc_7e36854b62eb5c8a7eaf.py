@property...
"""docstring"""
if len(self.nodes) > 0:
parent = self.nodes[-1].proxy
parent = None
return parent
