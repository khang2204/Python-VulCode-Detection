def call(ident, ip):...
api.reset_local_state()
mocked_ident[0] = ident
response = app.get('/request', extra_environ={'REMOTE_ADDR': ip},
    expect_errors=True)
return response.status_int
