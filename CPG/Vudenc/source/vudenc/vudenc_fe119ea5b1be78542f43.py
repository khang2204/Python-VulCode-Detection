def test_get_authenticated_routes(self):...
app = webapp2.WSGIApplication([webapp2.Route('/authenticated',
    Authenticated), webapp2.Route('/not-authenticated', NotAuthenticated)])
routes = handler.get_authenticated_routes(app)
self.assertEqual(1, len(routes))
self.assertEqual(Authenticated, routes[0].handler)
