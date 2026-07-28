def deserialize(self, data):...
self.__init__(gen_uuid=False)
self.name = data.get('name')
self.vars = data.get('vars', dict())
self.address = data.get('address', '')
self._uuid = data.get('uuid', None)
self.implicit = data.get('implicit', False)
groups = data.get('groups', [])
for group_data in groups:
g = Group()
g.deserialize(group_data)
self.groups.append(g)
