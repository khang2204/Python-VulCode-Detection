def reset(self):...
"""docstring"""
backend = pq.backends.ClassicalSimulator(**self.filter_kwargs_for_backend(
    self.kwargs))
self.eng = pq.MainEngine(backend)
super().reset()
