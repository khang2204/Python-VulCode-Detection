def run(self, name):...
if name:
return self.error()
return Account._by_name(name)
