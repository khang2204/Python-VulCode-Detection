def test_ftp_usage(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('ftplib.py', expect)
