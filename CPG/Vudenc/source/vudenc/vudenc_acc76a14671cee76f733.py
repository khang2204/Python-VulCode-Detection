def get_ui_routes():...
"""docstring"""
routes = []
for cls in _ui_navbar_tabs:
routes.extend(cls.get_webapp2_routes())
routes.extend([webapp2.Route('/auth', MainHandler), webapp2.Route(
    '/auth/bootstrap', BootstrapHandler, name='bootstrap'), webapp2.Route(
    '/auth/bootstrap/oauth', BootstrapOAuthHandler), webapp2.Route(
    '/auth/link', LinkToPrimaryHandler)])
return routes
