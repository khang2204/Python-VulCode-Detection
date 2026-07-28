def execute_queued(self):...
"""docstring"""
for operation in self._queue:
if operation.name not in operator_map:
result = self.expectation(self._observe.name, self._observe.wires)
par = [(x.val if isinstance(x, Variable) else x) for x in operation.params]
self._deallocate()
self.apply(operation.name, operation.wires, *par)
return result
