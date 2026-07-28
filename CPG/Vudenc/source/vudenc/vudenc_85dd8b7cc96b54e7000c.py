def test_get_volume_stats(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
self.driver._eql_execute('pool', 'select', self.configuration.eqlx_pool, 'show'
    ).AndReturn(['TotalCapacity: 111GB', 'FreeSpace: 11GB'])
self.mox.ReplayAll()
stats = self.driver.get_volume_stats(refresh=True)
self.assertEqual(stats['total_capacity_gb'], float('111.0'))
self.assertEqual(stats['free_capacity_gb'], float('11.0'))
self.assertEqual(stats['vendor_name'], 'Dell')
