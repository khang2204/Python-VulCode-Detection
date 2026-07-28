def log_out_callback(self, clear_session_on_errors=True):...
"""docstring"""
logging.debug('Processing SAML logout response')
auth = self._saml_auth()
errors = []
auth.process_slo()
errors = auth.get_errors()
if errors:
if clear_session_on_errors:
logging.info('SAML SLO request was successful')
self.clear_session()
return self._render_saml_errors_json(auth)
self.clear_session()
return self.redirect_to_goodbye()
