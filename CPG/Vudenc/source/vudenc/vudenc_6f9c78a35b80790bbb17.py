def setUp(self):...
self.objects = load_model_objects()
if settings.TEST_BROWSER == 'firefox':
self.browser = webdriver.Firefox()
self.browser = webdriver.Chrome()
log_karyn_in(self)
