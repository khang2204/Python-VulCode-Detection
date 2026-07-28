def test_temporary_file_without_cleanup(self):...
self.assertTrue(os.path.exists(fp.name),
    'Temporary file should exist within the context.')
self.assertTrue(os.path.exists(fp.name),
    'Temporary file should exist outside of context if cleanup=False.')
os.unlink(fp.name)
