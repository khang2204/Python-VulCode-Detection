def test_complete_prefix(self):...
self._tab_after('h')
eq_(self.terminal.method_calls, [('write', ('el',), {})])
self.terminal.reset_mock()
self.oms_ssh.handle_TAB()
eq_(self.terminal.method_calls, [('write', ('',), {}), ('nextLine', (), {}),
    ('write', ('help  hello\n',), {}), ('write', (self.oms_ssh.ps[0] +
    'hel',), {})])
