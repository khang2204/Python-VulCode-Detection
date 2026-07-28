def test_terminate_connection(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
volume = {'name': self.volume_name}
self.driver._eql_execute('volume', 'select', volume['name'], 'access',
    'delete', '1')
self.mox.ReplayAll()
self.driver.terminate_connection(volume, self.connector)
