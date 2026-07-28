"""
Django settings for the Deis project.
"""
from __future__ import unicode_literals
import os.path
import sys
import tempfile
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS
CONN_MAX_AGE = 60 * 3
ALLOWED_HOSTS = ['localhost']
TIME_ZONE = 'America/Denver'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = os.path.abspath(os.path.join(__file__, '..', '..', 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder')
SECRET_KEY = None
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader')
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'deis.context_processors.site')
MIDDLEWARE_CLASSES = ('django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'api.middleware.VersionMiddleware')
ROOT_URLCONF = 'deis.urls'
WSGI_APPLICATION = 'deis.wsgi.application'
TEMPLATE_DIRS = PROJECT_ROOT + '/web/templates',
INSTALLED_APPS = ('django.contrib.admin', 'django.contrib.auth',
    'django.contrib.contenttypes', 'django.contrib.humanize',
    'django.contrib.messages', 'django.contrib.sessions',
    'django.contrib.sites', 'django.contrib.staticfiles', 'django_fsm',
    'guardian', 'json_field', 'gunicorn', 'rest_framework', 'south', 'api',
    'web')
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend')
ANONYMOUS_USER_ID = -1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_USERNAME_BLACKLIST = ['system']
LOGIN_URL = '/api/auth/login/'
LOGIN_REDIRECT_URL = '/'
SOUTH_TESTS_MIGRATE = False
REST_FRAMEWORK = {'DEFAULT_MODEL_SERIALIZER_CLASS':
    'rest_framework.serializers.ModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',), 'PAGINATE_BY': 100
    }
APPEND_SLASH = False
if os.path.exists('/dev/log'):
SYSLOG_ADDRESS = '/dev/log'
if os.path.exists('/var/log/syslog'):
LOGGING = {'version': 1, 'disable_existing_loggers': False, 'formatters': {
    'verbose': {'format':
    '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    }, 'simple': {'format': '%(levelname)s %(message)s'}}, 'filters': {
    'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},
    'handlers': {'null': {'level': 'DEBUG', 'class': 'logging.NullHandler'},
    'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler',
    'formatter': 'simple'}, 'mail_admins': {'level': 'ERROR', 'filters': [
    'require_debug_false'], 'class': 'django.utils.log.AdminEmailHandler'},
    'rsyslog': {'class': 'logging.handlers.SysLogHandler', 'address':
    SYSLOG_ADDRESS, 'facility': 'local0'}}, 'loggers': {'django': {
    'handlers': ['null'], 'level': 'INFO', 'propagate': True},
    'django.request': {'handlers': ['console', 'mail_admins'], 'level':
    'WARNING', 'propagate': True}, 'api': {'handlers': ['console',
    'mail_admins', 'rsyslog'], 'level': 'INFO', 'propagate': True}}}
SYSLOG_ADDRESS = '/var/log/syslog'
SYSLOG_ADDRESS = 'localhost', 514
TEST_RUNNER = 'api.tests.SilentDjangoTestSuiteRunner'
ETCD_HOST, ETCD_PORT = os.environ.get('ETCD', '127.0.0.1:4001').split(',')[0
    ].split(':')
DEIS_LOG_DIR = os.path.abspath(os.path.join(__file__, '..', '..', 'logs'))
LOG_LINES = 1000
TEMPDIR = tempfile.mkdtemp(prefix='deis')
DEFAULT_BUILD = 'deis/helloworld'
DEIS_DOMAIN = 'deisapp.local'
SCHEDULER_MODULE = 'mock'
SCHEDULER_TARGET = ''
SCHEDULER_AUTH = ''
SCHEDULER_OPTIONS = {}
SSH_PRIVATE_KEY = ''
SECRET_KEY = os.environ.get('DEIS_SECRET_KEY',
    'CHANGEME_sapm$s%upvsw5l_zuy_&29rkywd^78ff(qi')
BUILDER_KEY = os.environ.get('DEIS_BUILDER_KEY',
    'CHANGEME_sapm$s%upvsw5l_zuy_&29rkywd^78ff(qi')
REGISTRY_MODULE = 'registry.mock'
REGISTRY_URL = 'http://localhost:5000'
REGISTRY_HOST = 'localhost'
REGISTRY_PORT = 5000
REGISTRATION_ENABLED = True
WEB_ENABLED = False
DATABASES = {'default': {'ENGINE': 'django.db.backends.' + os.environ.get(
    'DATABASE_ENGINE', 'postgresql_psycopg2'), 'NAME': os.environ.get(
    'DATABASE_NAME', 'deis')}}
APP_URL_REGEX = '[a-z0-9-]+'
ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = 'HTTP_X_FORWARDED_PROTO', 'https'
from .local_settings import *
if os.path.exists('/templates/confd_settings.py'):
sys.path.append('/templates')
from confd_settings import *
