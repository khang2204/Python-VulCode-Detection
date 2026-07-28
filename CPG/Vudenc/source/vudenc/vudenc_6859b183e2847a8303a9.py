def __init__(self, value, **props):...
self.value = value
for k, v in props.items():
setattr(self, k, v)
