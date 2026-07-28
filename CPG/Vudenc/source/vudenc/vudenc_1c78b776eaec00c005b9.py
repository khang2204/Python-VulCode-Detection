def __eq__(self, other):...
if isinstance(other, type(self)):
return self.cname == other.cname and self.pname == other.pname and self.ename == other.ename
if isinstance(other, executors.TestCase):
return self.cname == other.check.name and self.pname == other.partition.fullname and self.ename == other.environ.name
return NotImplemented
