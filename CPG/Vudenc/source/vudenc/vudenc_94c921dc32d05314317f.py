def get_frontend_routes():...
endpoints_services = [legacy_api.BuildBucketApi, config_api.ConfigApi,
    swarmbucket_api.SwarmbucketApi]
routes = [webapp2.Route('/', MainHandler), webapp2.Route(
    '/b/<build_id:\\d+>', BuildRPCHandler), webapp2.Route(
    '/build/<build_id:\\d+>', ViewBuildHandler)]
routes.extend(endpoints_webapp2.api_routes(endpoints_services))
routes.extend(endpoints_webapp2.api_routes(endpoints_services, base_path=
    '/api'))
prpc_server = prpc.Server()
prpc_server.add_interceptor(auth.prpc_interceptor)
prpc_server.add_service(access.AccessServicer())
prpc_server.add_service(api.BuildsApi())
routes += prpc_server.get_routes()
return routes
