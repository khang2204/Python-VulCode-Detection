middlewares=[
        session_middleware,
        # csrf_middleware,
        error_middleware,
    ]
)
app['config'] = config

setup_jinja(app, loader=PackageLoader('sqli', 'templates'),
            context_processors=[csrf_processor, auth_user_processor],
            autoescape=False)
setup_database(app)
setup_redis(app)
setup_routes(app)

return app
