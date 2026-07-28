def _history_get(self, cr, uid, ids, name, args, context={}):...
result = {}
for task in self.browse(cr, uid, ids, context=context):
result[task.id] = self._str_get(task, border='===')
return result
t2 = task.parent_id
level = 0
while t2:
level -= 1
t3 = map(lambda x: (x, 1), task.child_ids)
result[task.id] = self._str_get(t2, level) + result[task.id]
while t3:
t2 = t2.parent_id
t2 = t3.pop(0)
result[task.id] = result[task.id] + self._str_get(t2[0], t2[1])
t3 += map(lambda x: (x, t2[1] + 1), t2[0].child_ids)
