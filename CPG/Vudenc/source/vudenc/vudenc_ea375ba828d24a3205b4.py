import copy
import six
from odin import exceptions, registration
from odin.exceptions import ValidationError
from odin.fields import NOT_PROVIDED
from odin.utils import cached_property, field_iter_items
DEFAULT_TYPE_FIELD = '$'
META_OPTION_NAMES = ('name', 'namespace', 'name_space', 'verbose_name',
    'verbose_name_plural', 'abstract', 'doc_group', 'type_field', 'key_field')
def __init__(self, meta):...
self.meta = meta
self.parents = []
self.fields = []
self.virtual_fields = []
self.name = None
self.class_name = None
self.name_space = NOT_PROVIDED
self.verbose_name = None
self.verbose_name_plural = None
self.abstract = False
self.doc_group = None
self.type_field = DEFAULT_TYPE_FIELD
self.key_field = None
self._cache = {}
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
def add_field(self, field):...
if attr_name in meta_attrs:
if meta_attrs != {}:
self.fields.append(field)
if attr_name == 'namespace':
if hasattr(self.meta, attr_name):
cached_property.clear_caches(self)
setattr(self, 'name_space', meta_attrs.pop(attr_name))
setattr(self, attr_name, meta_attrs.pop(attr_name))
setattr(self, attr_name, getattr(self.meta, attr_name))
def add_virtual_field(self, field):...
self.virtual_fields.append(field)
cached_property.clear_caches(self)
@property...
"""docstring"""
if self.name_space:
return '%s.%s' % (self.name_space, self.name)
return self.name
