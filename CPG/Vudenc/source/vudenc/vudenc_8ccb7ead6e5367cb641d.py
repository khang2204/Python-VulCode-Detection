def run(self, fullname):...
if fullname:
return self.error()
return Thing._by_fullname(fullname, False, data=True)
