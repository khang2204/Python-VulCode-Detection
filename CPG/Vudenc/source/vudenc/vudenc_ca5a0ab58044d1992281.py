def _get_form_descriptions(request):...
"""docstring"""
return {'password_reset': get_password_reset_form().to_json(), 'login':
    get_login_session_form().to_json(), 'registration':
    RegistrationFormFactory().get_registration_form(request).to_json()}
