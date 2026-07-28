from django.utils.translation import string_concat
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy
from horizon import tables
from openstack_dashboard import api
from openstack_dashboard.usage import quotas
policy_rules = ('compute', 'os_compute_api:os-keypairs:delete'),
help_text = _(
    'Removing a key pair can leave OpenStack resources orphaned. You should not remove a key pair unless you are certain it is not being used anywhere.'
    )
@staticmethod...
return ungettext_lazy(u'Delete Key Pair', u'Delete Key Pairs', count)
