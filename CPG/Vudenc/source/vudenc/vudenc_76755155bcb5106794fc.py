import datetime
from django.core.exceptions import FieldDoesNotExist
from django.db.models import BooleanField, ForeignKey
from django.utils.formats import localize
from django.utils.html import format_html, escape
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _
from typing import List
from smart_lists.exceptions import SmartListException
from smart_lists.filters import SmartListFilter
def get_title(self):...
if self.label:
return self.label
if self.model_field:
return self.model_field.verbose_name.title()
if self.field_name == '__str__':
return self.model._meta.verbose_name.title()
field = getattr(self.model, self.field_name)
return self.field_name.title()
if callable(field) and getattr(field, 'short_description', False):
return field.short_description
return self.field_name.replace('_', ' ').title()
