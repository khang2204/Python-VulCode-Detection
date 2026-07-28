def test_list_devices_by_family(self):...
"""docstring"""
for fam in ('tape', 'disk', 'dir'):
for dev in client.devices.get(family=fam):
self.assertEqual(dev_family2str(dev.family), fam)
