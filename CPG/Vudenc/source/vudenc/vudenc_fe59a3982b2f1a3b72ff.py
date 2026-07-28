def test_config_file_generator(self):...
self.uut.executable = 'echo'
self.uut.config_file = lambda : ['config line1']
config_filename = self.uut.generate_config_file()
self.assertTrue(os.path.isfile(config_filename))
os.remove(config_filename)
self.uut.lint('filename')
