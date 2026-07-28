import json
from django.utils import safestring
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy
from horizon import tables
from openstack_dashboard import api
name = 'create'
verbose_name = _('Create Mapping')
url = 'horizon:identity:mappings:create'
classes = 'ajax-modal',
icon = 'plus'
policy_rules = ('identity', 'identity:create_mapping'),
name = 'edit'
verbose_name = _('Edit')
url = 'horizon:identity:mappings:update'
classes = 'ajax-modal',
icon = 'pencil'
policy_rules = ('identity', 'identity:update_mapping'),
@staticmethod...
return ungettext_lazy(u'Delete Mapping', u'Delete Mappings', count)
