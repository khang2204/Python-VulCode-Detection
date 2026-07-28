def before_feature(context, feature):...
context.browser = webdriver.PhantomJS()
context.browser.set_window_size(1280, 1024)
context.browser.implicitly_wait(DEFAULT_IMPLICIT_WAIT_TIMEOUT_IN_S)
context.browser.set_page_load_timeout(60)
context.browser.get(HOMEPAGE_URL)
