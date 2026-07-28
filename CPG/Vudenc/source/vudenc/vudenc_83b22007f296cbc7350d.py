from django.forms import SelectMultiple, Textarea
import django_filters
from re import split
from .models import event, injection, result, simics_register_diff
def fix_sort(string):...
return ''.join([(text.zfill(5) if text.isdigit() else text.lower()) for
    text in split('([0-9]+)', str(string))])
