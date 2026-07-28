def before_all(context):...
ensure_server()
logging.disable('INFO')
PixelatedSite.disable_csp_requests()
client = AppTestClient()
start_app_test_client(client, UserAgentMode(is_single_user=True))
client.listenTCP()
proxy = Proxy(proxy_port='8889', app_port='4567')
FeaturesResource.DISABLED_FEATURES.append('autoRefresh')
context.client = client
context.call_to_terminate_proxy = proxy.run_on_a_thread()
multi_user_client = AppTestClient()
start_app_test_client(multi_user_client, UserAgentMode(is_single_user=False))
multi_user_client.listenTCP(port=MULTI_USER_PORT)
context.multi_user_client = multi_user_client
