def check_example(self, example_script, expect, ignore_nosec=False):...
"""docstring"""
self.b_mgr.scores = []
self.run_example(example_script, ignore_nosec=ignore_nosec)
expected = 0
result = 0
for test_scores in self.b_mgr.scores:
for score_type in test_scores:
self.assertEqual(expected, result)
self.assertIn(score_type, expect)
for rating in expect[score_type]:
expected += expect[score_type][rating] * C.RANKING_VALUES[rating]
result += sum(test_scores[score_type])
