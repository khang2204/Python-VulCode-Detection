def test_ip_whitelist(self):...
"""docstring"""
ident1 = model.Identity(model.IDENTITY_USER, 'a@example.com')
ident2 = model.Identity(model.IDENTITY_USER, 'b@example.com')
model.bootstrap_ip_whitelist('whitelist', ['192.168.1.100/32'])
model.bootstrap_ip_whitelist_assignment(ident1, 'whitelist')
mocked_ident = [None]
@classmethod...
return [lambda _req: mocked_ident[0]]
