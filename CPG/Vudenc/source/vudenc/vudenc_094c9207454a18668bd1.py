import logging
import os
import urllib
import requests
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseForbidden, JsonResponse, FileResponse, HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Person, Candidate, Keyword, CommitteeMember
from .widgets import ID_VAL_SEPARATOR
BDR_EMAIL = 'bdr@brown.edu'
logger = logging.getLogger('etd')
def login(request):...
if request.user.is_authenticated():
next_url = request.GET.get('next', reverse('home'))
logger.error('login() - got anonymous user: %s' % request.META)
return HttpResponseRedirect(next_url)
return HttpResponseServerError(
    'Internet Server error. Please contact %s for assistance.' % BDR_EMAIL)
