def as_sql(self, compiler, connection, **kwargs):...
key_transforms = [self.key_name]
previous = self.lhs
while isinstance(previous, JsonKeyTransform):
key_transforms.insert(0, previous.key_name)
lhs, params = compiler.compile(previous)
previous = previous.lhs
if len(key_transforms) > 1:
return '(%s %s %%s)' % (lhs, self.nested_operator), [key_transforms] + params
int(self.key_name)
lookup = "'%s'" % self.key_name
lookup = '%s' % self.key_name
return '(%s %s %s)' % (lhs, self.operator, lookup), params
