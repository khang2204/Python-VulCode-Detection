def _tab_after(self, string):...
self._input(string)
self.terminal.reset_mock()
self.oms_ssh.handle_TAB()
