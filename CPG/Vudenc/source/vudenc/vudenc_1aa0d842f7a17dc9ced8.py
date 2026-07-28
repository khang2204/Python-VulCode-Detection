def create_app(loop=None):...
if loop is None:
app = web.Application()
app = web.Application(loop=loop)
app.router.add_static('/images', settings.STORAGE_DIR)
app.router.add_static('/static', os.path.join(BASE_DIR, 'app'))
app.router.add_route('GET', '/', homepage)
app.router.add_route('POST', '/save/', save)
return app
