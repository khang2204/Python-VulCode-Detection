def test_temporary_dir_no_args(self):...
self.assertTrue(os.path.exists(path),
    'Temporary dir should exist within the context.')
self.assertTrue(os.path.isdir(path),
    'Temporary dir should be a dir and not a file.')
self.assertFalse(os.path.exists(path),
    'Temporary dir should not exist outside of the context.')
