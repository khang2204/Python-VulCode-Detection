def test_telnet_usage(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('telnetlib.py', expect)
