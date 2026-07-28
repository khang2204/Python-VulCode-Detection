def __init__(self, rel_model, reference=None, related_name=None, on_delete=...
super(ForeignKeyField, self).__init__(*args, **kwargs)
self.rel_model = rel_model
self.reference = reference or rel_model._meta.fields['id']
self.related_name = related_name
self.on_delete = on_delete
self.on_update = on_update
