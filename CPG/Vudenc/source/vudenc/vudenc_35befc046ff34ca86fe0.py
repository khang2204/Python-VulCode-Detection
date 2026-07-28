def test_get_space_in_gb(self):...
self.assertEqual(self.driver._get_space_in_gb('123.0GB'), 123.0)
self.assertEqual(self.driver._get_space_in_gb('123.0TB'), 123.0 * 1024)
self.assertEqual(self.driver._get_space_in_gb('1024.0MB'), 1.0)
