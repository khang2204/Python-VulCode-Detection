def is_newer_than(self, other):...
if self.etag != other.etag or self.etag is None:
return cmp(self.mtime, other.mtime) > 0
return False
