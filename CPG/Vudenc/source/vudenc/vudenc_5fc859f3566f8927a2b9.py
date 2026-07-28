from django.utils.translation import string_concat, ugettext_lazy as _
from django.utils.text import format_lazy
from django.utils.functional import lazy as _lazy
from lib.helpers import Enum
def _format_lazy(format_string, *args, **kwargs):...
"""
Base permission classes.

These classes use same interface than ones in django-rest-framework and
are usable with APIViews too. We define our superclass so we don't need to
depend on django-rest-framework.
"""
return format_string.format(*args, **kwargs)
SAFE_METHODS = 'GET', 'HEAD', 'OPTIONS'
"""
    FilterBackend interface
    """
def filter_queryset(self, request, queryset, view):...
"""docstring"""
def get_fields(self, view):...
return []
