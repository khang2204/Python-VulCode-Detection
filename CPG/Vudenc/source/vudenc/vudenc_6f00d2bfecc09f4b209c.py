def test_manipulate_empty(self):...
"""docstring"""
client.devices.insert([])
client.devices.insert(None)
client.devices.delete([])
client.devices.delete(None)
client.media.insert([])
client.media.insert(None)
client.media.delete([])
client.media.delete(None)
