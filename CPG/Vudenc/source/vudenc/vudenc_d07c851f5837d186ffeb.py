def __next__(self):...
if self._resource_iters:
if self._field_iters:
if self._field_iters[-1]:
if self.current_resource:
field = self._field_iters[-1][0]
self._field_iters.pop()
if hasattr(self, 'on_exit'):
key, next_resource = next(self._resource_iters[-1])
self._path.pop()
if key is not None:
self._resource_iters.append(field.item_iter_from_object(self.current_resource))
self.on_exit()
self._resource_iters.pop()
_, _, field = self._path[-1]
self._field_iters.append(list(next_resource._meta.composite_fields))
self._path.append((NotSupplied, NotSupplied, field.name))
self._resource_stack.pop()
self._path[-1] = key, NotSupplied, field
self._resource_stack[-1] = next_resource
self._resource_stack.append(None)
return next(self)
if hasattr(self, 'on_enter'):
self._field_iters[-1].pop(0)
self.on_enter()
return next_resource
