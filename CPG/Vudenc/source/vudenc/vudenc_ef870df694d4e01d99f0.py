import json
from django.contrib.postgres import forms, lookups
from django.contrib.postgres.fields.array import ArrayField
from django.core import exceptions
from django.db.models import Field, TextField, Transform
from django.utils.translation import gettext_lazy as _
from .mixins import CheckFieldDefaultMixin
__all__ = ['HStoreField']
empty_strings_allowed = False
description = _('Map of strings to strings/nulls')
default_error_messages = {'not_a_string': _(
    'The value of “%(key)s” is not a string or null.')}
_default_hint = 'dict', '{}'
def db_type(self, connection):...
return 'hstore'
