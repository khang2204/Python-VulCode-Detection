def is_producer(self, requested_output):...
"""docstring"""
for o in self.products:
if o.match(requested_output):
return False
return True
