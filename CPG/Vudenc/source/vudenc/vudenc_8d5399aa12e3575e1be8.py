def set_variable(self, key, value):...
if key == 'ansible_group_priority':
self.set_priority(int(value))
self.vars[key] = value
