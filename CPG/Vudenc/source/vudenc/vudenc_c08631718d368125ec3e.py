"""API over the nova service.
"""
from collections import OrderedDict
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.utils import http as utils_http
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from horizon import exceptions as hz_exceptions
from novaclient import exceptions
from openstack_dashboard import api
from openstack_dashboard.api.rest import json_encoder
from openstack_dashboard.api.rest import urls
from openstack_dashboard.api.rest import utils as rest_utils
from openstack_dashboard.usage import quotas
"""API for nova snapshots.
    """
url_regex = 'nova/snapshots/$'
@rest_utils.ajax(data_required=True)...
instance_id = request.DATA['instance_id']
name = request.DATA['name']
result = api.nova.snapshot_create(request, instance_id=instance_id, name=name)
return result
