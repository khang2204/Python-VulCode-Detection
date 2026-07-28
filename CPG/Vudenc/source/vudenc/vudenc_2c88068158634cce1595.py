def test_create_volume_from_snapshot(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
snapshot = {'name': 'fakesnap', 'volume_name': 'fakevolume_name'}
volume = {'name': self.volume_name}
self.driver._eql_execute('volume', 'select', snapshot['volume_name'],
    'snapshot', 'select', snapshot['name'], 'clone', volume['name']).AndReturn(
    ['iSCSI target name is %s.' % self.fake_iqn])
self.mox.ReplayAll()
model_update = self.driver.create_volume_from_snapshot(volume, snapshot)
self.assertEqual(model_update, self._model_update)
