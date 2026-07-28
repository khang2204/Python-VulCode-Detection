def test_nested_pushd(self):...
pre_cwd = os.getcwd()
self.assertEqual(os.path.realpath(tempdir1), os.getcwd())
self.assertEqual(os.path.realpath(tempdir2), os.getcwd())
self.assertEqual(os.path.realpath(tempdir1), os.getcwd())
self.assertEqual(os.path.realpath(tempdir1), os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
