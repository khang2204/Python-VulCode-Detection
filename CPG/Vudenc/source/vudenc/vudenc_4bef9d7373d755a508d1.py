def same_checkout(self, other):...
if isinstance(other, GitSubproject) and (self.url, self.ref, self.conf.get(
return True
return False
