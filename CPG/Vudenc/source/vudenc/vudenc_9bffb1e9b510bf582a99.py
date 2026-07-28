"""View-related code common to the whole app."""
import functools
import re
import django.http
import django.utils.decorators
import django.views
import config
import const
import resources
import site_settings
import utils
"""Base view class shared across the app."""
ACTION_ID = None
_GET_PARAMETERS = {'lang': utils.strip}
def setup(self, request, *args, **kwargs):...
"""docstring"""
self.params = utils.Struct()
self.read_params(get_params=BaseView._GET_PARAMETERS)
self.env = utils.Struct()
self.env.repo = kwargs.get('repo', None)
self.env.action = self.ACTION_ID
self.env.config = config.Configuration(self.env.repo or '*')
lang = self.params.get('lang') or self.request.LANGUAGE_CODE
lang = re.sub('[^A-Za-z0-9-]', '', lang)
lang = const.LANGUAGE_SYNONYMS.get(lang, lang)
if lang in const.LANGUAGE_ENDONYMS.keys():
self.env.lang = lang
self.env.lang = self.env.config.language_menu_options[0
    ] if self.env.config.language_menu_options else const.DEFAULT_LANGUAGE_CODE
self.env.rtl = self.env.lang in const.LANGUAGES_BIDI
self.env.charset = const.CHARSET_UTF8
self.env.global_url = self.build_absolute_uri('/global')
def read_params(self, get_params=None, post_params=None, file_params=None):...
"""docstring"""
if self.request.method == 'GET':
if get_params:
if post_params:
for key, validator in get_params.items():
def _request_is_for_prefixed_path(self):...
for key, validator in post_params.items():
if file_params:
if key in self.request.GET:
"""docstring"""
if key in self.request.POST:
for key, validator in file_params.items():
setattr(self.params, key, validator(self.request.GET[key]))
if not site_settings.OPTIONAL_PATH_PREFIX:
setattr(self.params, key, validator(self.request.POST[key]))
if key in self.request.FILES:
return False
req_path = self.request.path[1:]
setattr(self.params, key, validator(self.request.FILES[key]))
if req_path == site_settings.OPTIONAL_PATH_PREFIX:
return True
return req_path.startswith('%s/' % site_settings.OPTIONAL_PATH_PREFIX)
