def _current_user_nameid(self):...
"""docstring"""
if 'saml_data' in session:
return session['saml_data']['nameid']
