def tearDown(self):...
os.environ.pop('SWARMING_BOT_ID', None)
os.chdir(self.old_cwd)
file_path.rmtree(self.root_dir)
super(TestBotMain, self).tearDown()
