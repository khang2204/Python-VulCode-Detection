def main(global_config, **settings):...
"""docstring"""
init_DBSession(settings)
config = pyramid.config.Configurator(settings=settings, root_factory=
    TraversalGlobalRootFactory)
def assert_settings_keys(keys):...
for settings_key in key:
assert config.registry.settings.get(settings_key)
config.include('pyramid_mako')
for key in config.registry.settings.keys():
value = os.getenv(key.replace('.', '_').upper(), ''
    ) or config.registry.settings[key]
config.add_request_method(partial(session_identity, session_keys={'id',
    'admin', 'faves', 'user'}), 'session_identity', reify=True)
config.registry.settings[key] = convert_str_with_type(value)
setup_pyramid_autoformater(config)
config.add_translation_dirs(config.registry.settings['i18n.translation_dirs'])
session_settings = extract_subkeys(config.registry.settings, 'session.')
session_factory = SignedCookieSessionFactory(serializer=json_serializer, **
    session_settings)
config.set_session_factory(session_factory)
if not config.registry.settings['server.etag.cache_buster']:
from .model.actions import last_update
import karakara.views.search
config.registry.settings['server.etag.cache_buster'
    ] = 'last_update:{0}'.format(str(last_update()))
karakara.views.search.search_config = read_json(config.registry.settings[
    'karakara.search.view.config'])
assert karakara.views.search.search_config, 'search_config data required'
def recv(self, *args, **kwargs):...
socket_manager = NullAuthEchoServerManager()
if config.registry.settings.get('karakara.websocket.port'):
def authenticator(key):...
config.registry['socket_manager'] = socket_manager
"""docstring"""
from .views.comunity_login import social_login
request = pyramid.request.Request({'HTTP_COOKIE': '{0}={1}'.format(config.
    registry.settings['session.cookie_name'], key)})
social_login.user_store = ComunityUserStore()
session_data = session_factory(request)
login_providers = config.registry.settings.get('login.provider.enabled')
return session_data and session_data.get('admin')
if 'facebook' in login_providers:
assert_settings_keys(('login.facebook.appid', 'login.facebook.secret'),
    message=
    'To use facebook as a login provider appid and secret must be provided')
if 'google' in login_providers:
social_login.add_login_provider(FacebookLogin(appid=config.registry.
    settings.get('login.facebook.appid'), secret=config.registry.settings.
    get('login.facebook.secret'), permissions=config.registry.settings.get(
    'login.facebook.permissions')))
social_login.add_login_provider(GoogleLogin(client_secret_file=config.
    registry.settings.get('login.google.client_secret_file')))
if not login_providers and config.registry.settings.get('karakara.server.mode'
social_login.add_login_provider(NullLoginProvider())
template_helpers.javascript_inline['comunity'] = social_login.html_includes
social_login.user_store = NullComunityUserStore()
def settings_path(key):...
path = os.path.join(os.getcwd(), config.registry.settings[key])
if not os.path.isdir(path):
log.error(f'Unable to add_static_view {key}:{path}')
return path
