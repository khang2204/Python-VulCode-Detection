def _get_form_descriptions(request):...
"""docstring"""
return {'login': _local_server_get('/user_api/v1/account/login_session/',
    request.session), 'registration': _local_server_get(
    '/user_api/v1/account/registration/', request.session),
    'password_reset': _local_server_get(
    '/user_api/v1/account/password_reset/', request.session)}
