def get_authenticated_routes(app):...
"""docstring"""
routes = list(app.router.match_routes)
routes.extend(v for k, v in app.router.build_routes.iteritems() if v not in
    app.router.match_routes)
return [r for r in routes if issubclass(r.handler, AuthenticatingHandler)]
