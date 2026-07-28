def serialize(self):...
groups = []
for group in self.groups:
groups.append(group.serialize())
return dict(name=self.name, vars=self.vars.copy(), address=self.address,
    uuid=self._uuid, groups=groups, implicit=self.implicit)
