@auth.require(acl.is_bot)...
self.response.headers['Content-Type'] = 'text/x-python'
self.response.headers['Content-Disposition'
    ] = 'attachment; filename="swarming_bot_bootstrap.py"'
self.response.out.write(bot_code.get_bootstrap(self.request.host_url).content)
