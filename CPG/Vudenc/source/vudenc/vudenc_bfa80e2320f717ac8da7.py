from os.path import abspath, dirname, join
from django.utils.translation import ugettext_lazy as _
BASE_DIR = dirname(dirname(abspath(__file__)))
DEBUG = False
SECRET_KEY = None
ADMINS = ()
EMAIL_TIMEOUT = 30
ALLOWED_HOSTS = ['*']
SITEWIDE_ALERT_TEXT = None
BRAND_NAME = 'A+'
WELCOME_TEXT = 'Welcome to A+ <small>modern learning environment</small>'
SHIBBOLETH_TITLE_TEXT = 'Aalto University users'
SHIBBOLETH_BODY_TEXT = (
    'Log in with Aalto University user account by clicking the button below. Programme students and faculty must login here.'
    )
SHIBBOLETH_BUTTON_TEXT = 'Aalto Login'
MOOC_TITLE_TEXT = 'Users external to Aalto'
MOOC_BODY_TEXT = (
    'Some of our courses are open for everyone. Login with your user account from one of the following services.'
    )
LOGIN_TITLE_TEXT = ''
LOGIN_BODY_TEXT = ''
LOGIN_BUTTON_TEXT = 'Maintenance login'
INTERNAL_USER_LABEL = 'Aalto'
EXTERNAL_USER_LABEL = 'MOOC'
WELCOME_TEXT_FI = 'A+ <small>verkkopohjainen oppimisympäristö</small>'
SHIBBOLETH_TITLE_TEXT_FI = 'Aalto-yliopiston käyttäjät'
SHIBBOLETH_BODY_TEXT_FI = (
    'Kirjaudu palveluun Aalto-yliopiston käyttäjätunnuksella alla olevasta painikkeesta. Koulutusohjelmien opiskelijoiden ja henkilökunnan pitää kirjautua tästä.'
    )
SHIBBOLETH_BUTTON_TEXT_FI = 'Aalto-kirjautuminen'
MOOC_TITLE_TEXT_FI = 'Käyttäjät Aallon ulkopuolelta'
MOOC_BODY_TEXT_FI = (
    'Osa kursseistamme on avoinna kaikille. Kirjaudu sisään jonkin seuraavan palvelun käyttäjätunnuksellasi.'
    )
LOGIN_TITLE_TEXT_FI = ''
LOGIN_BODY_TEXT_FI = ''
LOGIN_BUTTON_TEXT_FI = 'Ylläpidon kirjautuminen'
TRACKING_HTML = ''
EXCEL_CSV_DEFAULT_DELIMITER = ';'
EXERCISE_HTTP_TIMEOUT = 15
EXERCISE_HTTP_RETRIES = 5, 5, 5
EXERCISE_ERROR_SUBJECT = 'A+ exercise error in {course}: {exercise}'
EXERCISE_ERROR_DESCRIPTION = """
As a course teacher or technical contact you were automatically emailed by A+ about the error incident. A student could not access or submit an exercise because the grading service used is offline or unable to produce valid response.

{message}

Open the exercise:
  {exercise_url}
Edit course email settings:
  {course_edit_url}

****************************************
Error trace:
****************************************

{error_trace}

****************************************
Request fields:
****************************************

{request_fields}
"""
INSTALLED_APPS = ('django.contrib.contenttypes',
    'django.contrib.staticfiles', 'django.contrib.sessions',
    'django.contrib.messages', 'django.contrib.admin',
    'django.contrib.auth', 'django.contrib.humanize', 'bootstrapform',
    'rest_framework', 'rest_framework.authtoken', 'inheritance',
    'userprofile', 'authorization', 'course', 'exercise', 'edit_course',
    'deviations', 'notification', 'external_services', 'news', 'threshold',
    'diploma', 'apps', 'redirect_old_urls', 'js_jquery_toggle',
    'django_colortag')
SHIBBOLETH_VARIABLES_URL_ENCODED = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
MIDDLEWARE_CLASSES = ('django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lib.middleware.SqlInjectionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware')
ROOT_URLCONF = 'aplus.urls'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/accounts/login/'
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [join(BASE_DIR, 'local_templates'), join(BASE_DIR, 'templates')
    ], 'APP_DIRS': True, 'OPTIONS': {'context_processors': [
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.contrib.messages.context_processors.messages']}}]
FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',)
WSGI_APPLICATION = 'aplus.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME':
    join(BASE_DIR, 'aplus.db'), 'USER': '', 'PASSWORD': '', 'HOST': '',
    'PORT': ''}}
CACHES = {'default': {'BACKEND': 'lib.cache.backends.LocMemCache',
    'TIMEOUT': None, 'OPTIONS': {'MAX_SIZE': 1000000}}}
LANGUAGE_CODE = 'en-gb'
LANGUAGES = [('en', 'English'), ('fi', 'Finnish')]
TIME_ZONE = 'EET'
USE_I18N = True
USE_L10N = True
USE_TZ = True
FORMAT_MODULE_PATH = 'aplus'
LOCALE_PATHS = join(BASE_DIR, 'locale'),
STATICFILES_STORAGE = 'lib.storage.BumpStaticFilesStorage'
STATICFILES_DIRS = join(BASE_DIR, 'assets'),
STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'lib.api.authentication.grader.GraderAuthentication',
    'rest_framework.authentication.SessionAuthentication'),
    'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
    'userprofile.permissions.GraderUserCanOnlyRead'),
    'DEFAULT_RENDERER_CLASSES': ('lib.api.core.APlusJSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer'),
    'DEFAULT_CONTENT_NEGOTIATION_CLASS':
    'lib.api.core.APlusContentNegotiation', 'DEFAULT_VERSIONING_CLASS':
    'lib.api.core.APlusVersioning', 'PAGE_SIZE': 100, 'DEFAULT_VERSION':
    '2', 'ALLOWED_VERSIONS': {'1': '1.0', '2': '2.0'}}
OVERRIDE_SUBMISSION_HOST = None
REMOTE_PAGE_HOSTS_MAP = None
MAX_UNOFFICIAL_SUBMISSIONS = 200
TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
TEST_OUTPUT_VERBOSE = True
TEST_OUTPUT_DESCRIPTIONS = True
TEST_OUTPUT_DIR = 'test_results'
from lib.logging import skip_unreadable_post
LOGGING = {'version': 1, 'disable_existing_loggers': False, 'formatters': {
    'verbose': {'format':
    '[%(asctime)s: %(levelname)s/%(module)s] %(message)s'}, 'colored': {
    '()': 'r_django_essentials.logging.SourceColorizeFormatter', 'format':
    '[%(asctime)s: %(levelname)s/%(module)s] %(message)s', 'colors': {
    'django.db.backends': {'fg': 'cyan'}, 'django.db.deferred': {'fg':
    'yellow'}, 'cached': {'fg': 'red'}}}}, 'filters': {
    'skip_unreadable_post': {'()': 'django.utils.log.CallbackFilter',
    'callback': skip_unreadable_post}, 'require_debug_true': {'()':
    'django.utils.log.RequireDebugTrue'}, 'require_debug_false': {'()':
    'django.utils.log.RequireDebugFalse'}}, 'handlers': {'debug_console': {
    'level': 'DEBUG', 'filters': ['require_debug_true'], 'class':
    'logging.StreamHandler', 'stream': 'ext://sys.stdout', 'formatter':
    'colored'}, 'console': {'level': 'DEBUG', 'class':
    'logging.StreamHandler', 'stream': 'ext://sys.stdout', 'formatter':
    'verbose'}, 'email': {'level': 'ERROR', 'filters': [
    'require_debug_false', 'skip_unreadable_post'], 'class':
    'django.utils.log.AdminEmailHandler'}, 'mail_admins': {'level': 'ERROR',
    'filters': ['require_debug_false', 'skip_unreadable_post'], 'class':
    'django.utils.log.AdminEmailHandler'}}, 'loggers': {'': {'level':
    'INFO', 'handlers': ['console', 'email'], 'propagate': True}, 'django':
    {'level': 'INFO', 'handlers': ['console', 'email']}, 'py.warnings': {
    'handlers': ['console']}}}
from os import environ
from r_django_essentials.conf import *
update_settings_with_file(__name__, environ.get('APLUS_LOCAL_SETTINGS',
    'local_settings'), quiet='APLUS_LOCAL_SETTINGS' in environ)
update_settings_from_environment(__name__, 'DJANGO_')
update_settings_from_environment(__name__, 'APLUS_')
update_secret_from_file(__name__, environ.get('APLUS_SECRET_KEY_FILE',
    'secret_key'))
if not BASE_URL:
if 'INSTALLED_LOGIN_APPS' in globals():
INSTALLED_APPS = INSTALLED_LOGIN_APPS + INSTALLED_APPS
use_cache_template_loader_in_production(__name__)
SOCIAL_AUTH = False
AUTHENTICATION_BACKENDS = 'django.contrib.auth.backends.ModelBackend',
if 'shibboleth_login' in INSTALLED_APPS:
AUTHENTICATION_BACKENDS += (
    'shibboleth_login.auth_backend.ShibbolethAuthBackend',)
if 'social_django' in INSTALLED_APPS:
SOCIAL_AUTH = True
if DEBUG:
AUTHENTICATION_BACKENDS += 'social_core.backends.google.GoogleOAuth2',
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'
    ] += 'rest_framework.authentication.BasicAuthentication',
from lib.models import install_defer_logger
install_defer_logger()
