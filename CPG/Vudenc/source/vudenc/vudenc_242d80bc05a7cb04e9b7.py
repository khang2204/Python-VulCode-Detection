def test_delete_snapshot(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
snapshot = {'name': 'fakesnap', 'volume_name': 'fakevolume_name'}
self.driver._eql_execute('volume', 'select', snapshot['volume_name'],
    'snapshot', 'delete', snapshot['name'])
self.mox.ReplayAll()
self.driver.delete_snapshot(snapshot)
