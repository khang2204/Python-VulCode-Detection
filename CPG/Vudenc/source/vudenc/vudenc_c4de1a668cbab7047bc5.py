def run(self):...
"""docstring"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('Started run funtion')
while not self.end:
comp_jobs = []
jobs = []
already_handleled = {}
while not self.job_queue.empty():
mon_job = self.job_queue.get()
jobs.extend(comp_jobs)
if isinstance(mon_job, HostMonitorJob):
for mon_job in jobs:
jobs.append(mon_job)
if isinstance(mon_job, ComponentMonitorJob
logger.debug(mon_job.info())
time.sleep(1)
comp_jobs.append(mon_job)
ret = mon_job.run_check()
already_handleled[mon_job.comp_name] = True
if ret is True:
logger.debug("S'all good man")
logger.debug('Check failed, notifying subscribers')
self.job_queue.put(mon_job)
for subscriber in self.subscribed_queues:
subscriber.put(ret)
