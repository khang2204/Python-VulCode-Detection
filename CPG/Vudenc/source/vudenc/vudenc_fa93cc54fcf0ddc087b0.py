def test_ensure_export(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
volume = {'name': self.volume_name, 'size': 1}
self.driver._eql_execute('volume', 'select', volume['name'], 'show')
self.mox.ReplayAll()
self.driver.ensure_export({}, volume)
