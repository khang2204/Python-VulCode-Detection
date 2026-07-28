@trial_timeout(5)...
"""docstring"""
def on_callback(response):...
self.assertEqual(response, magnet_link)
magnet_link = 'magnet:?xt=urn:btih:DC4B96CF85A85CEEDB8ADC4B96CF85A85CEEDB8A'
port = get_random_port()
self.setUpHttpRedirectServer(port, magnet_link)
test_url = 'http://localhost:%d' % port
http_deferred = http_get(test_url).addCallback(on_callback)
return http_deferred
