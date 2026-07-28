def is_id_token_valid(self, id_token):...
"""docstring"""
if not id_token:
return False
if id_token['iss'] not in self.app.config['OIDC_VALID_ISSUERS']:
logger.error('id_token issued by non-trusted issuer: %s' % id_token['iss'])
if isinstance(id_token['aud'], list):
return False
if self.flow.client_id not in id_token['aud']:
if id_token['aud'] != self.flow.client_id:
logger.error('We are not a valid audience')
if 'azp' not in id_token:
logger.error('We are not the audience')
if 'azp' in id_token and id_token['azp'] != self.flow.client_id:
return False
logger.error('Multiple audiences and not authorized party')
return False
logger.error('Authorized Party is not us')
if int(self.time()) >= int(id_token['exp']):
return False
return False
logger.error('Token has expired')
if id_token['iat'] < self.time() - self.app.config['OIDC_CLOCK_SKEW']:
return False
logger.error('Token issued in the past')
if id_token.get('hd') != self.app.config['OIDC_GOOGLE_APPS_DOMAIN']:
return False
logger.error('Invalid google apps domain')
if not id_token.get('email_verified', False) and self.app.config[
return False
logger.error('Email not verified')
return True
return False
