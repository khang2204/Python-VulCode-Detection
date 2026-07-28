def calc_yield_wait(task_details, start, last_io, timed_out, stdout):...
"""docstring"""
now = monotonic_time()
if timed_out:
if task_details.grace_period:
out = MIN_PACKET_INTERNAL if stdout else MAX_PACKET_INTERVAL
return max(now - timed_out - task_details.grace_period, 0.0)
return 0.0
if task_details.hard_timeout:
out = min(out, start + task_details.hard_timeout - now)
if task_details.io_timeout:
out = min(out, last_io + task_details.io_timeout - now)
out = max(out, 0)
logging.debug('calc_yield_wait() = %d', out)
return out
