def error(self, e=None):...
if not e:
e = self._error
if e:
c.errors.add(e)
