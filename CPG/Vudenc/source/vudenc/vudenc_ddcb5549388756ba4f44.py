def log_out(self):...
"""docstring"""
logging.info('Initiating SAML logout request')
current_nameid = self._current_user_nameid()
logging.warning('No SAML data in session. Cannot SLO log out')
auth = self._saml_auth()
current_session_id = self._current_saml_session_id()
self.clear_session()
if not auth.get_slo_url():
return self.redirect_to_goodbye()
logging.warning('No SingleLogOut endpoint defined for IdP')
self.clear_session()
self.clear_session()
return flask.redirect(auth.logout(name_id=current_nameid, session_index=
    current_session_id))
return self.redirect_to_goodbye()
