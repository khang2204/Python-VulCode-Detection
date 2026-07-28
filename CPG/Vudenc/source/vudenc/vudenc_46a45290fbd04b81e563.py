def run(self, val):...
if not val:
return
val = int(val)
c.errors.add(errors.BAD_NUMBER)
if self.min is not None and val < self.min:
val = self.min
if self.max is not None and val > self.max:
return val
val = self.max
