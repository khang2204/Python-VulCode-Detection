def stop_webdriver():...
test = get_executing_test()
webdriver = getattr(test, 'webdriver', None)
if webdriver:
test.webdriver = None
webdriver.close()
