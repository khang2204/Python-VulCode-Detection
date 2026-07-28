def contribute_to_class(self, cls, name):...
cls._meta = self
self.name = cls.__name__
self.class_name = '%s.%s' % (cls.__module__, cls.__name__)
if self.meta:
meta_attrs = self.meta.__dict__.copy()
if not self.verbose_name:
for name in self.meta.__dict__:
self.verbose_name = self.name.replace('_', ' ').strip('_ ')
if not self.verbose_name_plural:
if name.startswith('_'):
for attr_name in META_OPTION_NAMES:
self.verbose_name_plural = self.verbose_name + 's'
if attr_name in meta_attrs:
if meta_attrs != {}:
if attr_name == 'namespace':
if hasattr(self.meta, attr_name):
setattr(self, 'name_space', meta_attrs.pop(attr_name))
setattr(self, attr_name, meta_attrs.pop(attr_name))
setattr(self, attr_name, getattr(self.meta, attr_name))
