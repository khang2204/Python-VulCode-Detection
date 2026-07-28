def test_create_snapshot(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
snapshot = {'name': 'fakesnap', 'volume_name': 'fakevolume_name'}
snap_name = 'fake_snap_name'
self.driver._eql_execute('volume', 'select', snapshot['volume_name'],
    'snapshot', 'create-now').AndReturn(['Snapshot name is %s' % snap_name])
self.driver._eql_execute('volume', 'select', snapshot['volume_name'],
    'snapshot', 'rename', snap_name, snapshot['name'])
self.mox.ReplayAll()
self.driver.create_snapshot(snapshot)
