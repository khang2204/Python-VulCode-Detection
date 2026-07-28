ap = ArgumentParser()
commandline.standard_argparse_options(ap, default_config='./config/dev.yaml')
options = ap.parse_args(argv)

config = commandline.config_from_options(options, CONFIG_SCHEMA)

app = Application(
    debug=True,
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
