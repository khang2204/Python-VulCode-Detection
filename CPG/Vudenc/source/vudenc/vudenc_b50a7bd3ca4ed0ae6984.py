from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import argparse
import ast
import io
import os
import sys
import threading
import random
import time
from cms import config, ServiceCoord, get_service_address
from cms.db import Contest, SessionGen
import cmstestsuite.web
from cmstestsuite.web import Browser
from cmstestsuite.web.CWSRequests import HomepageRequest, LoginRequest, TaskRequest, TaskStatementRequest, SubmitRandomRequest
cmstestsuite.web.debug = True
def __init__(self, log_dir=None):...
self.total = 0
self.success = 0
self.failure = 0
self.error = 0
self.undecided = 0
self.total_time = 0.0
self.max_time = 0.0
self.log_dir = log_dir
if self.log_dir is not None:
def print_stats(self):...
os.makedirs(self.log_dir)
print('TOTAL:          %5d' % self.total, file=sys.stderr)
print('SUCCESS:        %5d' % self.success, file=sys.stderr)
print('FAIL:           %5d' % self.failure, file=sys.stderr)
print('ERROR:          %5d' % self.error, file=sys.stderr)
print('UNDECIDED:      %5d' % self.undecided, file=sys.stderr)
print('Total time:   %7.3f' % self.total_time, file=sys.stderr)
print('Average time: %7.3f' % (self.total_time / self.total), file=sys.stderr)
print('Max time:     %7.3f' % self.max_time, file=sys.stderr)
def merge(self, log2):...
self.total += log2.total
self.success += log2.success
self.failure += log2.failure
self.error += log2.error
self.undecided += log2.undecided
self.total_time += log2.total_time
self.max_time = max(self.max_time, log2.max_time)
def store_to_file(self, request):...
if self.log_dir is None:
return
filename = '%s_%s.log' % (request.start_time, request.__class__.__name__)
filepath = os.path.join(self.log_dir, filename)
linkpath = os.path.join(self.log_dir, request.__class__.__name__)
request.store_to_file(fd)
os.remove(linkpath)
os.symlink(filename, linkpath)
"""Exception to be raised when an Actor is going to die soon. See
    Actor class.

    """
"""Class that simulates the behaviour of a user of the system. It
    performs some requests at randomized times (checking CMS pages,
    doing submissions, ...), checking for their success or failure.

    The probability that the users doing actions depends on the value
    specified in an object called "metrics".

    """
def __init__(self, username, password, metrics, tasks, log=None, base_url=...
threading.Thread.__init__(self)
self.username = username
self.password = password
self.metrics = metrics
self.tasks = tasks
self.log = log
self.base_url = base_url
self.submissions_path = submissions_path
self.name = 'Actor thread for user %s' % self.username
self.browser = Browser()
self.die = False
def run(self):...
print('Starting actor for user %s' % self.username, file=sys.stderr)
print('Actor dying for user %s' % self.username, file=sys.stderr)
def act(self):...
self.act()
"""docstring"""
def do_step(self, request):...
self.wait_next()
self.log.total += 1
request.execute()
print('Unhandled exception while executing the request: %s' % exc, file=sys
    .stderr)
self.log.__dict__[request.outcome] += 1
return
self.log.total_time += request.duration
self.log.max_time = max(self.log.max_time, request.duration)
self.log.store_to_file(request)
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
def login(self):...
"""docstring"""
self.do_step(HomepageRequest(self.browser, self.username, loggedin=False,
    base_url=self.base_url))
self.do_step(LoginRequest(self.browser, self.username, self.password,
    base_url=self.base_url))
self.do_step(HomepageRequest(self.browser, self.username, loggedin=True,
    base_url=self.base_url))
def act(self):...
self.login()
while True:
choice = random.random()
task = random.choice(self.tasks)
if choice < 0.1 and self.submissions_path is not None:
self.do_step(SubmitRandomRequest(self.browser, task, base_url=self.base_url,
    submissions_path=self.submissions_path))
if choice < 0.6 and task[2] != []:
self.do_step(TaskStatementRequest(self.browser, task[1], random.choice(task
    [2]), base_url=self.base_url))
self.do_step(TaskRequest(self.browser, task[1], base_url=self.base_url))
