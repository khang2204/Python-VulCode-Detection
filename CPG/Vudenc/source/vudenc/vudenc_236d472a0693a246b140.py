def add_to_model(self, model_class, name):...
self.name = name
self.model_class = model_class
self.related_name = self.related_name or '%ss' % model_class._meta.name
model_class._meta.add_field(self)
if self.related_name in self.rel_model._meta.fields:
print('ERROR: Foreign key conflict')
if self.related_name in self.rel_model._meta.reverse_rel:
print('ERROR: Foreign key %s already exists on model %s' % (self.
    related_name, model_class._meta.name))
self.model_class._meta.rel[self.name] = self
self.model_class._meta.rel_class[self.rel_model] = self
reference = ReferenceField(self.model_class)
reference.add_to_model(self.rel_model, self.related_name, self.name)
