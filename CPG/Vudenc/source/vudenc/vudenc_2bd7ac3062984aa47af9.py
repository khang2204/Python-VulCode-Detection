def test_get_state(self):...
self.mock(time, 'time', lambda : 126.0)
expected = os_utilities.get_state()
expected['sleep_streak'] = 12
for disk in expected['disks'].itervalues():
self.assertGreater(disk.pop('free_mb'), 1.0)
actual = bot_main.get_state(None, 12)
for disk in actual['disks'].itervalues():
self.assertGreater(disk.pop('free_mb'), 1.0)
self.assertGreater(actual.pop('nb_files_in_temp'), 0)
self.assertGreater(expected.pop('nb_files_in_temp'), 0)
self.assertGreater(actual.pop('uptime'), 0)
self.assertGreater(expected.pop('uptime'), 0)
self.assertEqual(sorted(expected.pop('temp', {})), sorted(actual.pop('temp',
    {})))
self.assertEqual(expected, actual)
