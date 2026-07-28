def setUp(self):...
self.oms_ssh = OmsSshProtocol()
self.terminal = mock.Mock()
self.oms_ssh.terminal = self.terminal
self.oms_ssh.connectionMade()
self.orig_commands = cmd.commands
cmd.commands = lambda : dict(hello=cmd.Cmd, **self.orig_commands())
