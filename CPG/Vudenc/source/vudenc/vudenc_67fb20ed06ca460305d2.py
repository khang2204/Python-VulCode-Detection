def test_extend_volume(self):...
new_size = '200'
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
volume = {'name': self.volume_name, 'size': 100}
self.driver._eql_execute('volume', 'select', volume['name'], 'size', '%sG' %
    new_size)
self.mox.ReplayAll()
self.driver.extend_volume(volume, new_size)
