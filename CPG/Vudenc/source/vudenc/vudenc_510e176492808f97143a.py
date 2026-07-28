import json
from django.contrib.postgres import lookups
from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.postgres.validators import ArrayMaxLengthValidator
from django.core import checks, exceptions
from django.db.models import Field, IntegerField, Transform
from django.db.models.lookups import Exact, In
from django.utils.translation import gettext_lazy as _
from ..utils import prefix_validation_error
from .mixins import CheckFieldDefaultMixin
from .utils import AttributeSetter
__all__ = ['ArrayField']
empty_strings_allowed = False
default_error_messages = {'item_invalid': _(
    'Item %(nth)s in the array did not validate:'), 'nested_array_mismatch':
    _('Nested arrays must have the same length.')}
_default_hint = 'list', '[]'
def __init__(self, base_field, size=None, **kwargs):...
self.base_field = base_field
self.size = size
if self.size:
self.default_validators = [*self.default_validators,
    ArrayMaxLengthValidator(self.size)]
if hasattr(self.base_field, 'from_db_value'):
self.from_db_value = self._from_db_value
super().__init__(**kwargs)
@property...
return self.__dict__['model']
@model.setter...
self.__dict__['model'] = model
self.base_field.model = model
def check(self, **kwargs):...
errors = super().check(**kwargs)
if self.base_field.remote_field:
errors.append(checks.Error(
    'Base field for array cannot be a related field.', obj=self, id=
    'postgres.E002'))
base_errors = self.base_field.check()
return errors
if base_errors:
messages = '\n    '.join('%s (%s)' % (error.msg, error.id) for error in
    base_errors)
errors.append(checks.Error("""Base field for array has errors:
    %s""" %
    messages, obj=self, id='postgres.E001'))
