def test_simple_pushd(self):...
pre_cwd = os.getcwd()
self.assertEqual(tempdir, path)
self.assertEqual(os.path.realpath(tempdir), os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
