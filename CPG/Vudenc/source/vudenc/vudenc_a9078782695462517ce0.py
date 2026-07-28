def get_next_or_prev(models, item, direction):...
"""docstring"""
getit = False
if direction == 'prev':
models = models.reverse()
for m in models:
if getit:
if getit:
return m
if item == m:
return models[0]
return False
getit = True
