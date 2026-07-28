def setUp(self):...
self.assertTrue(self.client.login(username='autotest', password='password'))
chaos.CREATE_ERROR_RATE = 0
chaos.DESTROY_ERROR_RATE = 0
chaos.START_ERROR_RATE = 0
chaos.STOP_ERROR_RATE = 0
settings.SCHEDULER_MODULE = 'chaos'
settings.SSH_PRIVATE_KEY = '<some-ssh-private-key>'
