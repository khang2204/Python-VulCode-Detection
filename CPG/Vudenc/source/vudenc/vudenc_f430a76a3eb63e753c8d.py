def run_on_a_thread(self, logfile='/tmp/app_test_client.log', port=4567,...
def _start():...
self.listenTCP(port, host)
reactor.run()
process = multiprocessing.Process(target=_start)
process.start()
time.sleep(1)
return lambda : process.terminate()
