from pykeg.core import models
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
def process_view(self, request, view_func, view_args, view_kwargs):...
"""docstring"""
kbsite_name = view_kwargs.pop('kbsite_name', None)
if not kbsite_name:
kbsite_name = 'default'
request.kbsite = models.KegbotSite.objects.get(name=kbsite_name)
return None
