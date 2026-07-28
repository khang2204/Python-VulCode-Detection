def test_delete_volume(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
volume = {'name': self.volume_name, 'size': 1}
self.driver._eql_execute('volume', 'select', volume['name'], 'show')
self.driver._eql_execute('volume', 'select', volume['name'], 'offline')
self.driver._eql_execute('volume', 'delete', volume['name'])
self.mox.ReplayAll()
self.driver.delete_volume(volume)
