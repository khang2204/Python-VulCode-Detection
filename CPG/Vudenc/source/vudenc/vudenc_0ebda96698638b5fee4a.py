def run(self, title):...
if not title:
if self.emp_error is not None:
if len(title) > self.length:
c.errors.add(self.emp_error)
c.errors.add(self.len_error)
return title
