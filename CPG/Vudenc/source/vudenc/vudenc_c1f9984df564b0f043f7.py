def run(self, val):...
if not val:
c.errors.add(self.error)
val = float(val)
c.errors.add(self.error)
return
if self.min is not None and val < self.min:
val = self.min
if self.max is not None and val > self.max:
return val
val = self.max
