def setUp(self):...
super(FunctionalTests, self).setUp()
path = os.path.join(os.getcwd(), 'bandit', 'plugins')
b_conf = b_config.BanditConfig()
self.b_mgr = b_manager.BanditManager(b_conf, 'file')
self.b_mgr.b_conf._settings['plugins_dir'] = path
self.b_mgr.b_ts = b_test_set.BanditTestSet(config=b_conf)
