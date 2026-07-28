def wait_next(self):...
"""docstring"""
SLEEP_PERIOD = 0.1
time_to_wait = self.metrics['time_coeff'] * random.expovariate(self.metrics
    ['time_lambda'])
sleep_num = int(time_to_wait / SLEEP_PERIOD)
remaining_sleep = time_to_wait - sleep_num * SLEEP_PERIOD
for i in xrange(sleep_num):
time.sleep(SLEEP_PERIOD)
time.sleep(remaining_sleep)
if self.die:
if self.die:
