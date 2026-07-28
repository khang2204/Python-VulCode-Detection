import re
from django.utils.translation import ugettext_lazy as _
from horizon import exceptions
from horizon import forms
from horizon import messages
from openstack_dashboard import api
NEW_LINES = re.compile('\\r|\\n')
KEYPAIR_NAME_REGEX = re.compile('^\\w+(?:[- ]\\w+)*$', re.UNICODE)
KEYPAIR_ERROR_MESSAGES = {'invalid': _(
    'Key pair name may only contain letters, numbers, underscores, spaces, and hyphens and may not be white space.'
    )}
name = forms.RegexField(max_length=255, label=_('Key Pair Name'), regex=
    KEYPAIR_NAME_REGEX, error_messages=KEYPAIR_ERROR_MESSAGES)
def handle(self, request, data):...
return True
