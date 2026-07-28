def invert(self, orig):...
if PY2:
return {v: k for k, v in orig.iteritems()}
return {v: k for k, v in orig.items()}
