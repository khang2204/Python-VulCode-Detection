def constant_prefix(self):...
first_wildcard = _wildcard_regex.search(self.file)
if first_wildcard:
return self.file[:first_wildcard.start()]
return self.file
