def start_website(purpose):...
config = load_website_config(purpose)
http_handler = create_website_http_handler(purpose, config)
io_loop = IOLoop.instance()
io_loop.add_callback(lambda : LOGGER.info('started website {}'.format(purpose))
    )
start_http_server(http_handler, io_loop=io_loop, host=config.host, port=
    config.port)
