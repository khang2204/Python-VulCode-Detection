def remove_observer(self, func):...
"""docstring"""
i = 0
while i < len(self.observers):
ofunc = self.observers[i][0]
if ofunc == func:
i += 1
