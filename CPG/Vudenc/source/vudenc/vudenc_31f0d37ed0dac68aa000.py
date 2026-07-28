def expected_requests(self, requests):...
"""docstring"""
requests = requests[:]
for request in requests:
self.assertEqual(tuple, request.__class__)
self.assertEqual([], self._requests)
self.assertIn(len(request), (3, 4))
self._requests = requests
