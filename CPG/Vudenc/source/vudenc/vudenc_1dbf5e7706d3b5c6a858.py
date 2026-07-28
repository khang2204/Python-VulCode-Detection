def create_frontend_app():...
template.bootstrap({'templates': os.path.join(THIS_DIR, 'templates')})
routes = get_routes()
routes.extend(handlers_endpoints.get_routes())
return webapp2.WSGIApplication(routes)
