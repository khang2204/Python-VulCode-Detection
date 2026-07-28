def test_metric_gathering(self):...
expect = {'nosec': 2, 'loc': 7, 'issues': {'CONFIDENCE': {'HIGH': 5},
    'SEVERITY': {'LOW': 5}}}
self.check_metrics('skip.py', expect)
expect = {'nosec': 0, 'loc': 4, 'issues': {'CONFIDENCE': {'HIGH': 2},
    'SEVERITY': {'LOW': 2}}}
self.check_metrics('imports.py', expect)
