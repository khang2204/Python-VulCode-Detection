def test_temporary_dir_without_cleanup(self):...
self.assertTrue(os.path.exists(path),
    'Temporary dir should exist within the context.')
self.assertTrue(os.path.exists(path),
    'Temporary dir should exist outside of context if cleanup=False.')
shutil.rmtree(path)
