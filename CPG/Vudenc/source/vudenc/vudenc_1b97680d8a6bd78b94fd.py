def check_is_test_failed(test):...
message = getattr(test, 'error', None)
if message is not None:
stop_browser()
test.fail(message)
