def test_temporary_file_no_args(self):...
self.assertTrue(os.path.exists(fp.name),
    'Temporary file should exist within the context.')
self.assertTrue(os.path.exists(fp.name) == False,
    'Temporary file should not exist outside of the context.')
