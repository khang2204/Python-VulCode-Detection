def gae_cookie_authentication(_request):...
"""docstring"""
user = users.get_current_user()
return model.Identity(model.IDENTITY_USER, user.email()) if user else None
