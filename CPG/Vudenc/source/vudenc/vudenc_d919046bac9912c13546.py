def test_do_setup(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
fake_group_ip = '10.1.2.3'
for feature in ('confirmation', 'paging', 'events', 'formatoutput'):
self.driver._eql_execute('cli-settings', feature, 'off')
self.driver._eql_execute('grpparams', 'show').AndReturn([
    'Group-Ipaddress: %s' % fake_group_ip])
self.mox.ReplayAll()
self.driver.do_setup(self._context)
self.assertEqual(fake_group_ip, self.driver._group_ip)
