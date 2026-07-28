import base64
import decimal
import pickle
from django.contrib.postgres.lookups import Unaccent
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CharField, Lookup, TextField, Transform, lookups
from django.utils.translation import ugettext_lazy as _
from common.utils import json_decode, json_encode
is_postgresql = lambda connection: connection.vendor == 'postgresql'
is_mysql = lambda connection: connection.vendor == 'mysql'
is_sqlite = lambda connection: connection.vendor == 'sqlite'
"""
    Champ décimal spécifique pour éviter la représentation scientifique
    """
def value_from_object(self, obj):...
value = super().value_from_object(obj)
if isinstance(value, decimal.Decimal):
return self._transform_decimal(value)
return value
