def test_delete_absent_volume(self):...
self.driver._eql_execute = self.mox.CreateMock(self.driver._eql_execute)
volume = {'name': self.volume_name, 'size': 1, 'id': self.volid}
self.driver._eql_execute('volume', 'select', volume['name'], 'show').AndRaise(
    processutils.ProcessExecutionError(stdout=
    """% Error ..... does not exist.
"""))
self.mox.ReplayAll()
self.driver.delete_volume(volume)
