def same_checkout(self, other):...
if isinstance(other, SvnSubproject) and (self.url, self.rev) == (other.url,
return True
return False
