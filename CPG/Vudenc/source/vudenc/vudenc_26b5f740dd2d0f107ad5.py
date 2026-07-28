def test_update_volume_stats(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
self.driver._eql_execute('pool', 'select', self.configuration.eqlx_pool, 'show'
    ).AndReturn(['TotalCapacity: 111GB', 'FreeSpace: 11GB'])
self.mox.ReplayAll()
self.driver._update_volume_stats()
self.assertEqual(self.driver._stats['total_capacity_gb'], 111.0)
self.assertEqual(self.driver._stats['free_capacity_gb'], 11.0)
