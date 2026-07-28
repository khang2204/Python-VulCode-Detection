@web.middleware
async def session_middleware(request, handler):
    """Wrapper to Session Middleware factory.
    """
    # Do the trick, by passing app & handler back to original session
    # middleware factory. Do not forget to await on results here as original
    # session middleware factory is also awaitable.
    app = request.app
    storage = RedisStorage(app['redis'], httponly=False)
    middleware = session_middleware_(storage)
    return await middleware(request, handler)


@web.middleware
async def csrf_middleware(request, handler):
    """Provides csrf"""
    if request.method == "POST":
        session = await get_session(request)
        token = session.pop('_csrf_token', None)
