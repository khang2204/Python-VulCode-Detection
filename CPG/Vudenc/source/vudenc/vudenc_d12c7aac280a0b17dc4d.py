def setUp(self):...
super(TestPaverBokChoyCmd, self).setUp()
self.shard = os.environ.get('SHARD')
self.env_var_override = EnvironmentVarGuard()
