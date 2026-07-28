"""Unit tests for phobos.dss"""
import sys
import unittest
import os
from random import randint
from phobos.core.dss import Client
from phobos.core.ffi import MediaInfo, DevInfo
from phobos.core.const import dev_family2str, PHO_DEV_DIR
"""
    This test case issue requests to the DSS to stress the python bindings.
    """
def test_client_connect(self):...
"""docstring"""
cli = Client()
cli.connect()
cli.disconnect()
def test_client_connect_refused(self):...
"""docstring"""
cli = Client()
environ_save = os.environ['PHOBOS_DSS_connect_string']
os.environ['PHOBOS_DSS_connect_string'
    ] = "dbname='tata', user='titi', password='toto'"
self.assertRaises(EnvironmentError, cli.connect)
os.environ['PHOBOS_DSS_connect_string'] = environ_save
def test_list_devices_by_family(self):...
"""docstring"""
for fam in ('tape', 'disk', 'dir'):
for dev in client.devices.get(family=fam):
def test_list_media(self):...
self.assertEqual(dev_family2str(dev.family), fam)
"""docstring"""
for mda in client.media.get():
self.assertTrue(isinstance(mda, MediaInfo))
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
def test_manipulate_empty(self):...
dev.host = 'localhost'
self.assertTrue(isinstance(retrieved_dev, dev.__class__))
"""docstring"""
dev.serial = '__TEST_MAGIC_%d' % randint(0, 1000000)
self.assertEqual(retrieved_dev.serial, dev.serial)
client.devices.insert([])
insert_list.append(dev)
client.devices.insert(None)
client.devices.delete([])
client.devices.delete(None)
client.media.insert([])
client.media.insert(None)
client.media.delete([])
client.media.delete(None)
def test_media_lock_unlock(self):...
"""docstring"""
label = '/some/path_%d' % randint(0, 1000000)
client.media.add(PHO_DEV_DIR, 'POSIX', None, label, locked=False)
media = client.media.get(id=label)[0]
self.assertFalse(media.is_locked())
client.media.lock([media])
client.media.lock([media])
media = client.media.get(id=label)[0]
self.assertTrue(media.is_locked())
client.media.unlock([media])
client.media.unlock([media])
media = client.media.get(id=label)[0]
self.assertFalse(media.is_locked())
if __name__ == '__main__':
unittest.main()
