def _saml_auth(self, req_dict=None):...
"""docstring"""
if req_dict is None:
req_dict = self._saml_req_dict_from_request()
auth = OneLogin_Saml2_Auth(req_dict, self.saml_config)
return auth
