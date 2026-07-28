def test_create_cloned_volume(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
src_vref = {'id': 'fake_uuid'}
volume = {'name': self.volume_name}
src_volume_name = self.configuration.volume_name_template % src_vref['id']
self.driver._eql_execute('volume', 'select', src_volume_name, 'clone',
    volume['name']).AndReturn(['iSCSI target name is %s.' % self.fake_iqn])
self.mox.ReplayAll()
model_update = self.driver.create_cloned_volume(volume, src_vref)
self.assertEqual(model_update, self._model_update)
