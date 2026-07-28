def stop_browser():...
test = get_executing_test()
if 'spynner' == test.browser_type:
stop_spynner_browser()
if test.browser_type in ['chrome', 'remote']:
stop_webdriver()
