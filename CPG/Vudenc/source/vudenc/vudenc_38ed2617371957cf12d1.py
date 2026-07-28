def check_metrics(self, example_script, expect):...
"""docstring"""
self.b_mgr.metrics = metrics.Metrics()
self.b_mgr.scores = []
self.run_example(example_script)
m = self.b_mgr.metrics.data
for k in expect:
if k != 'issues':
if 'issues' in expect:
self.assertEqual(expect[k], m['_totals'][k])
for criteria, default in C.CRITERIA:
for rank in C.RANKING:
label = '{0}.{1}'.format(criteria, rank)
expected = 0
if expect['issues'].get(criteria, None).get(rank, None):
expected = expect['issues'][criteria][rank]
self.assertEqual(expected, m['_totals'][label])
