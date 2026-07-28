def terminate():...
logger.info('Shutdown initiated')
send_to_wm([b'GLOBAL', b'WZWorker', b'terminate'])
for t in threading.enumerate():
if isinstance(t, threading.Timer):
logger.info('Exiting')
t.cancel()
