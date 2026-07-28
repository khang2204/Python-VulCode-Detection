def stop_spynner_browser():...
test = get_executing_test()
browser = test.spynner_browser
if browser:
test.spynner_browser = None
browser.close()
