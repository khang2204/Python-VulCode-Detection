from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import time
import threading
import traceback
import ray
LOG_POINT = 0
LOG_SPAN_START = 1
LOG_SPAN_END = 2
"""A log span context manager that does nothing"""
def __enter__(self):...
def __exit__(self, type, value, tb):...
NULL_LOG_SPAN = _NullLogSpan()
def profile(event_type, extra_data=None, worker=None):...
"""docstring"""
if worker is None:
worker = ray.worker.global_worker
return RayLogSpanRaylet(worker.profiler, event_type, extra_data=extra_data)
