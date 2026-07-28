def login(self):...
"""docstring"""
self.do_step(HomepageRequest(self.browser, self.username, loggedin=False,
    base_url=self.base_url))
self.do_step(LoginRequest(self.browser, self.username, self.password,
    base_url=self.base_url))
self.do_step(HomepageRequest(self.browser, self.username, loggedin=True,
    base_url=self.base_url))
