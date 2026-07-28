def oauth2_handle_error(remote, resp, error_code, error_uri, error_description...
"""docstring"""
flash('Authorization with remote service failed.')
return redirect('/')
