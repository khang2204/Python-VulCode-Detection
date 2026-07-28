import copy
import logging
from decimal import Decimal
import dateutil.parser
import pytz
import vat_moss.errors
import vat_moss.id
from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from pretix.base.forms.widgets import BusinessBooleanRadio, DatePickerWidget, SplitDateTimePickerWidget, TimePickerWidget, UploadedFileWidget
from pretix.base.models import InvoiceAddress, Question
from pretix.base.models.tax import EU_COUNTRIES
from pretix.base.settings import PERSON_NAME_SCHEMES
from pretix.base.templatetags.rich_text import rich_text
from pretix.control.forms import SplitDateTimeField
from pretix.helpers.i18n import get_format_without_seconds
from pretix.presale.signals import question_form_fields
logger = logging.getLogger(__name__)
widget = forms.TextInput
def __init__(self, scheme: dict, field: forms.Field, attrs=None):...
widgets = []
self.scheme = scheme
self.field = field
for fname, label, size in self.scheme['fields']:
a = copy.copy(attrs) or {}
super().__init__(widgets, attrs)
a['data-fname'] = fname
def decompress(self, value):...
widgets.append(self.widget(attrs=a))
if value is None:
return None
data = []
for i, field in enumerate(self.scheme['fields']):
fname, label, size = field
if '_legacy' in value and not data[-1]:
data.append(value.get(fname, ''))
data[-1] = value.get('_legacy', '')
return data
