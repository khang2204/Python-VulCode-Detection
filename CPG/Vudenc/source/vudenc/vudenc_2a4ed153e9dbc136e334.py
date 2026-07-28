def _render_saml_settings_dict(self):...
"""docstring"""
debug = app.config['SAML_DEBUG']
if debug is None:
debug = app.debug
root_url = app.config['SAML_CONFIDANT_URL_ROOT']
if not root_url:
root_url = root_url.rstrip('/')
name_id_fmt = 'urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress'
sp_data = {'entityId': root_url + '/v1/saml/metadata',
    'assertionConsumerService': {'url': root_url + '/v1/saml/consume',
    'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST'},
    'singleLogoutService': {'url': root_url + '/v1/saml/logout', 'binding':
    'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-REDIRECT'}, 'NameIDFormat':
    name_id_fmt}
sp_has_key = False
if app.config['SAML_SP_KEY_FILE']:
sp_has_key = True
if app.config['SAML_SP_KEY']:
sp_data['privateKey'] = self._load_rsa_for_saml(app.config[
    'SAML_SP_KEY_FILE'], password=app.config.get('SAML_SP_KEY_FILE_PASSWORD'))
sp_has_key = True
if app.config['SAML_SP_CERT_FILE']:
sp_data['privateKey'] = app.config['SAML_SP_KEY']
sp_data['x509cert'] = self._load_x509_for_saml(app.config['SAML_SP_CERT_FILE'])
if app.config['SAML_SP_CERT']:
sp_data['x509cert'] = app.config['SAML_SP_CERT']
security_data = {'nameIdEncrypted': False, 'authnRequestsSigned':
    sp_has_key, 'logoutRequestsSigned': sp_has_key, 'logoutResponsesSigned':
    app.config['SAML_SECURITY_SLO_RESP_SIGNED'], 'signMetadata': sp_has_key,
    'wantMessagesSigned': app.config['SAML_SECURITY_MESSAGES_SIGNED'],
    'wantAssertionsSigned': app.config['SAML_SECURITY_ASSERTIONS_SIGNED'],
    'wantNameIdEncrypted': False, 'signatureAlgorithm': app.config[
    'SAML_SECURITY_SIG_ALGO']}
idp_data = {'entityId': app.config['SAML_IDP_ENTITY_ID'],
    'singleSignOnService': {'url': app.config['SAML_IDP_SIGNON_URL'],
    'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'}}
if app.config['SAML_IDP_LOGOUT_URL']:
idp_data['singleLogoutService'] = {'url': app.config['SAML_IDP_LOGOUT_URL'],
    'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect'}
if app.config['SAML_IDP_CERT_FILE']:
idp_data['x509cert'] = self._load_x509_for_saml(app.config[
    'SAML_IDP_CERT_FILE'])
if app.config['SAML_IDP_CERT']:
idp_data['x509cert'] = app.config['SAML_IDP_CERT']
data = {'strict': True, 'debug': debug, 'sp': sp_data, 'idp': idp_data,
    'security': security_data}
if app.config['SAML_RAW_JSON_SETTINGS']:
logging.debug('overriding SAML settings from JSON')
logging.debug('Rendered SAML settings: {!r}'.format(data))
dict_deep_update(data, app.config['SAML_RAW_JSON_SETTINGS'])
return data
