def test_wait_time(self):...
"""docstring"""
start = time.time()
tournament.check_version((2, 4))
end = time.time()
count = round(end - start, 1)
self.assertEqual(count, 3.0)
