def start_spynner_browser(url, visible=False):...
test = get_executing_test()
test.spynner_browser = spynner.Browser(debug_level=spynner.DEBUG)
if visible:
test.spynner_browser.show(maximized=False)
test.spynner_browser.load(url)
while test.spynner_browser:
test.spynner_browser._events_loop()
test.error = 'keyboard interrupt'
check_is_test_failed(test)
