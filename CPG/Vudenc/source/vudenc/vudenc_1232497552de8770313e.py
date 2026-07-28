def run(self, val):...
if self.options and val not in self.options:
c.errors.add(errors.INVALID_OPTION)
return val
return self.default
