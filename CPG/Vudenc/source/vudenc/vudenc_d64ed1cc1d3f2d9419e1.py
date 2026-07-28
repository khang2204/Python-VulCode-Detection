import json
from psycopg2.extras import Json
from django.contrib.postgres import forms, lookups
from django.core import exceptions
from django.db.models import Field, TextField, Transform, lookups as builtin_lookups
from django.utils.translation import gettext_lazy as _
from .mixins import CheckFieldDefaultMixin
__all__ = ['JSONField']
"""
    Customized psycopg2.extras.Json to allow for a custom encoder.
    """
def __init__(self, adapted, dumps=None, encoder=None):...
self.encoder = encoder
super().__init__(adapted, dumps=dumps)
def dumps(self, obj):...
options = {'cls': self.encoder} if self.encoder else {}
return json.dumps(obj, **options)
