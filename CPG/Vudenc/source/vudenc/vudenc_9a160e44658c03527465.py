def test_create_volume(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
volume = {'name': self.volume_name, 'size': 1}
self.driver._eql_execute('volume', 'create', volume['name'], '%sG' % volume
    ['size'], 'pool', self.configuration.eqlx_pool, 'thin-provision'
    ).AndReturn(['iSCSI target name is %s.' % self.fake_iqn])
self.mox.ReplayAll()
model_update = self.driver.create_volume(volume)
self.assertEqual(model_update, self._model_update)
