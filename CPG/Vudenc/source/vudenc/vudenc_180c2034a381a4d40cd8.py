@wraps(view_func)...
if g.oidc_id_token is None:
return self.redirect_to_auth_server(request.url)
return view_func(*args, **kwargs)
