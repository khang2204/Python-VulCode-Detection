import time
from urllib.parse import urlencode
from urllib import urlencode
from django.core.exceptions import SuspiciousOperation
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string
from django.utils.module_loading import import_string
from django.views.generic import View
from mozilla_django_oidc.utils import absolutify, import_from_settings, is_authenticated
"""OIDC client authentication callback HTTP endpoint"""
http_method_names = ['get']
@property...
return import_from_settings('LOGIN_REDIRECT_URL_FAILURE', '/')
