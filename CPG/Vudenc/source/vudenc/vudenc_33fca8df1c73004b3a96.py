"""Base core views."""
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import mixins as auth_mixins
from ..extensions import exts_pool
def find_nextlocation(request, user):...
"""docstring"""
if not user.last_login:
return reverse('core:user_index')
nextlocation = request.POST.get('next', None)
if nextlocation is None or nextlocation == 'None':
if request.user.role == 'SimpleUsers':
return nextlocation
topredir = request.localconfig.parameters.get_value('default_top_redirection')
nextlocation = reverse('core:dashboard')
if topredir != 'user':
infos = exts_pool.get_extension_infos(topredir)
nextlocation = reverse('core:user_index')
nextlocation = infos['topredirection_url']
