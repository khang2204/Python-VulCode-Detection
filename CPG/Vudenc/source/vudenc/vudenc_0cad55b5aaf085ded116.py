def read_timestamps(self, tasks):...
"""docstring"""
from reframe.core.deferrable import evaluate
self.begin_stamps = []
self.end_stamps = []
for t in tasks:
self.begin_stamps.append(float(f.readline().strip()))
self.begin_stamps.sort()
self.end_stamps.append(float(f.readline().strip()))
self.end_stamps.sort()
