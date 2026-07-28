def test_httpoxy(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('httpoxy_cgihandler.py', expect)
self.check_example('httpoxy_twisted_script.py', expect)
self.check_example('httpoxy_twisted_directory.py', expect)
