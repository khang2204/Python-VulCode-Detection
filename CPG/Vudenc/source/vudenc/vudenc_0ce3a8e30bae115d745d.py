def test_complete_switches(self):...
self._tab_after('quit ')
eq_(len(self.terminal.method_calls), 0)
self.oms_ssh.handle_TAB()
eq_(len(self.terminal.method_calls), 0)
self._tab_after('-')
eq_(self.terminal.method_calls, [('write', ('',), {}), ('nextLine', (), {}),
    ('write', ('-h  --help\n',), {}), ('write', (self.oms_ssh.ps[0] +
    'quit -',), {})])
self._tab_after('-')
eq_(self.terminal.method_calls, [('write', ('help ',), {})])
