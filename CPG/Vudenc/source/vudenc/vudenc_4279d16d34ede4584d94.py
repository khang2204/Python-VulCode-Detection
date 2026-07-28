def start_browser(url, browser_type):...
if os.getenv('VEIL_REMOTE_BROWSER'):
browser_type = 'remote'
get_executing_test().browser_type = browser_type
test = get_executing_test()
test.addCleanup(stop_browser)
if 'spynner' == browser_type:
start_spynner_browser(url)
if 'chrome' == browser_type:
start_chrome_browser(url)
if 'remote' == browser_type:
command_executor = 'http://{}:4444/wd/hub'.format(os.getenv(
    'VEIL_REMOTE_BROWSER'))
start_remote_browser(url, command_executor)
