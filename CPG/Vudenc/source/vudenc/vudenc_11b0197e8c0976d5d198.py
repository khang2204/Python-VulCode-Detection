def test_ssh_execute_error(self):...
ssh = self.mox.CreateMock(paramiko.SSHClient)
chan = self.mox.CreateMock(paramiko.Channel)
transport = self.mox.CreateMock(paramiko.Transport)
self.mox.StubOutWithMock(self.driver, '_get_output')
self.mox.StubOutWithMock(ssh, 'get_transport')
self.mox.StubOutWithMock(chan, 'invoke_shell')
expected_output = ['Error: test run', '% Error']
ssh.get_transport().AndReturn(transport)
transport.open_session().AndReturn(chan)
chan.invoke_shell()
self.driver._get_output(chan).AndReturn(expected_output)
cmd = 'this is dummy command'
chan.send('stty columns 255' + '\r')
self.driver._get_output(chan).AndReturn(expected_output)
chan.send(cmd + '\r')
self.driver._get_output(chan).AndReturn(expected_output)
chan.close()
self.mox.ReplayAll()
self.assertRaises(processutils.ProcessExecutionError, self.driver.
    _ssh_execute, ssh, cmd)
