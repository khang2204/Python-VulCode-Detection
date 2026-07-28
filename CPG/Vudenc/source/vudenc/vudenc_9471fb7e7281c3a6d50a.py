def __init__(self, avatar=None):...
resource.Resource.__init__(self)
self.avatar = avatar
self.use_security_proxy = get_config().getboolean('auth', 'security_proxy_rest'
    )
