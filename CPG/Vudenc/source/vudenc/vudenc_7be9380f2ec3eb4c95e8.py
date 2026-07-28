def start_remote_browser(url, command_executor):...
test = get_executing_test()
capabilities = selenium.webdriver.DesiredCapabilities.INTERNETEXPLORER
test.webdriver = selenium.webdriver.Remote(command_executor,
    desired_capabilities=capabilities)
test.webdriver.get(url)
while test.webdriver:
time.sleep(0.1)
test.error = 'keyboard interrupt'
check_is_test_failed(test)
