def setUp(self):...
super(AuthenticatingHandlerTest, self).setUp()
api.reset_local_state()
self.logged_errors = []
self.mock(handler.logging, 'error', lambda *args, **kwargs: self.
    logged_errors.append((args, kwargs)))
self.logged_warnings = []
self.mock(handler.logging, 'warning', lambda *args, **kwargs: self.
    logged_warnings.append((args, kwargs)))
