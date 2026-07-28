def start_test_website(purpose, **kwargs):...
config = load_website_config(purpose)
http_handler = create_website_http_handler(purpose, **kwargs)
http_server = start_test_http_server(http_handler, host=config.host, port=
    config.port)
http_server.purpose = purpose
return http_server
