import collections
import csv
import functools
import io
import zipfile
from operator import attrgetter
import mimetypes
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import connection, models
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.views.decorators.gzip import gzip_page
from rest_framework import permissions
from rest_framework.views import APIView
from alice.authenticators import IsDataTeamServer
from ..constants import BREAKDOWN_TYPES
from ..models import Advisor, Breakdown, CustomerResponse, Notification, Win
from ..serializers import CustomerResponseSerializer, WinSerializer
from users.models import User
""" Endpoint returning CSV of all Win data, with foreign keys flattened """
permission_classes = permissions.IsAdminUser,
win_fields = WinSerializer().fields
customerresponse_fields = CustomerResponseSerializer().fields
IGNORE_FIELDS = ['responded', 'sent', 'country_name', 'updated', 'complete',
    'type', 'type_display', 'export_experience_display', 'location']
def __init__(self, **kwargs):...
self.users_map = {u.id: u for u in User.objects.all()}
prefetch_tables = [('advisors', Advisor), ('breakdowns', Breakdown), (
    'confirmations', CustomerResponse), ('notifications', Notification)]
self.table_maps = {}
for table, model in prefetch_tables:
prefetch_map = collections.defaultdict(list)
super().__init__(**kwargs)
instances = model.objects.all()
def _extract_breakdowns(self, win):...
if table == 'notifications':
"""docstring"""
instances = instances.filter(type='c').order_by('created')
for instance in instances:
breakdowns = self.table_maps['breakdowns'][win['id']]
prefetch_map[instance.win_id].append(instance)
self.table_maps[table] = prefetch_map
retval = []
for db_val, name in BREAKDOWN_TYPES:
type_breakdowns = [b for b in breakdowns if b.type == db_val]
return retval
type_breakdowns = sorted(type_breakdowns, key=attrgetter('year'))
for index in range(5):
breakdown = '{0}: £{1:,}'.format(type_breakdowns[index].year,
    type_breakdowns[index].value)
breakdown = None
retval.append(('{0} breakdown {1}'.format(name, index + 1), breakdown))
