def __init__(self, *args, **kwargs):...
super().__init__(*args, **kwargs)
for f in list(self.fields.keys()):
if f != 'name':
