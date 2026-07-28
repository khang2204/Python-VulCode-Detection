"""
Configuration (file) handling for eduID IdP.
"""
import os
import ConfigParser
_CONFIG_DEFAULTS = {'debug': False, 'syslog_debug': '0', 'num_threads': '8',
    'logdir': None, 'logfile': None, 'syslog_socket': None, 'listen_addr':
    '0.0.0.0', 'listen_port': '8088', 'pysaml2_config': 'idp_conf.py',
    'fticks_secret_key': None, 'fticks_format_string':
    'F-TICKS/SWAMID/2.0#TS={ts}#RP={rp}#AP={ap}#PN={pn}#AM={am}#',
    'static_dir': None, 'ssl_adapter': 'builtin', 'server_cert': None,
    'server_key': None, 'cert_chain': None, 'userdb_mongo_uri': None,
    'userdb_mongo_database': None, 'sso_session_lifetime': '15',
    'sso_session_mongo_uri': None, 'raven_dsn': None, 'content_packages': [
    ], 'verify_request_signatures': '0', 'status_test_usernames': [],
    'signup_link': '#', 'dashboard_link': '#', 'password_reset_link': '#',
    'default_language': 'en', 'base_url': None, 'default_eppn_scope': None,
    'authn_info_mongo_uri': None, 'max_authn_failures_per_month': '50',
    'login_state_ttl': '5', 'default_scoped_affiliation': None, 'vccs_url':
    'http://localhost:8550/', 'insecure_cookies': '0'}
_CONFIG_SECTION = 'eduid_idp'
"""
    Class holding IdP application configuration.

    Loads configuration from an INI-file at instantiation.

    :param filename: string, INI-file name
    :param debug: boolean, default debug value
    :raise ValueError: if INI-file can't be parsed
    """
def __init__(self, filename, debug):...
self._parsed_content_packages = None
self._parsed_status_test_usernames = None
self.section = _CONFIG_SECTION
_CONFIG_DEFAULTS['debug'] = str(debug)
cfgdir = os.path.dirname(filename)
_CONFIG_DEFAULTS['pysaml2_config'] = os.path.join(cfgdir, _CONFIG_DEFAULTS[
    'pysaml2_config'])
self.config = ConfigParser.ConfigParser(_CONFIG_DEFAULTS)
if not self.config.read([filename]):
@property...
"""docstring"""
return self.config.getint(self.section, 'num_threads')
