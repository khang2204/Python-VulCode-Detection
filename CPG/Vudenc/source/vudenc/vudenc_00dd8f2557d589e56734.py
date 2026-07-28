def test_complete_consumed_switches(self):...
self._tab_after('ls --help')
eq_(self.terminal.method_calls, [('write', (' ',), {})])
self._tab_after('-')
assert 'help' not in self.terminal.method_calls[2][1][0]
assert '-h' not in self.terminal.method_calls[2][1][0]
