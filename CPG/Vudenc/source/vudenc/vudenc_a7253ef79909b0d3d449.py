def test_getset(self):...
"""docstring"""
insert_list = []
for i in range(10):
dev = DevInfo()
client.devices.insert(insert_list)
dev.family = PHO_DEV_DIR
for dev in insert_list:
dev.model = ''
res = client.devices.get(serial=dev.serial)
client.devices.delete(res)
dev.path = '/tmp/test_%d' % randint(0, 1000000)
for retrieved_dev in res:
dev.host = 'localhost'
self.assertTrue(isinstance(retrieved_dev, dev.__class__))
dev.serial = '__TEST_MAGIC_%d' % randint(0, 1000000)
self.assertEqual(retrieved_dev.serial, dev.serial)
insert_list.append(dev)
