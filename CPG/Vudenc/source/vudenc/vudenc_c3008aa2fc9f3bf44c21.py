def setUp(self):...
super(TestBotMain, self).setUp()
os.environ.pop('SWARMING_LOAD_TEST', None)
self.root_dir = tempfile.mkdtemp(prefix='bot_main')
self.old_cwd = os.getcwd()
os.chdir(self.root_dir)
os.mkdir('logs')
self.server = xsrf_client.XsrfRemote('https://localhost:1/')
self.attributes = {'dimensions': {'foo': ['bar'], 'id': ['localhost'],
    'pool': ['default']}, 'state': {'cost_usd_hour': 3600.0}, 'version': '123'}
self.mock(zip_package, 'generate_version', lambda : '123')
self.bot = bot.Bot(self.server, self.attributes, 'https://localhost:1/',
    'version1', self.root_dir, self.fail)
self.mock(self.bot, 'post_error', self.fail)
self.mock(self.bot, 'restart', self.fail)
self.mock(subprocess42, 'call', self.fail)
self.mock(time, 'time', lambda : 100.0)
config_path = os.path.join(test_env_bot_code.BOT_DIR, 'config', 'config.json')
config = json.load(f)
self.mock(bot_main, 'get_config', lambda : config)
self.mock(bot_main, 'THIS_FILE', os.path.join(test_env_bot_code.BOT_DIR,
    'swarming_bot.zip'))
