def service_to_service_authentication(request):...
"""docstring"""
app_id = request.headers.get('X-Appengine-Inbound-Appid')
return model.Identity(model.IDENTITY_SERVICE, app_id) if app_id else None
