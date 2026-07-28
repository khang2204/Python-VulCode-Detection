def start_chrome_browser(url):...
test = get_executing_test()
old_cwd = os.getcwd()
os.chdir('/tmp')
test.webdriver = selenium.webdriver.Chrome()
os.chdir(old_cwd)
test.webdriver.get(url)
while test.webdriver:
time.sleep(0.1)
test.error = 'keyboard interrupt'
check_is_test_failed(test)
