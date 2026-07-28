def openid_cookie_authentication(request):...
"""docstring"""
user = openid.get_current_user(request)
return model.Identity(model.IDENTITY_USER, user.email) if user else None
