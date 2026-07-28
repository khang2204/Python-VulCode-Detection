def run(self):...
self.__sinit__()
if self.start_timer:
self.inter_sleep(self.start_timer)
if self.running:
self.log.info('Starting')
self.log.info('Aborted')
self.child = self.call[0](*self.call[1], **self.call[2])
self.log.warn(e)
self.log.info('Terminating')
self.running.set()
self.child(self)
self.log.exception(e)
self.unbind_methods()
self.running.clear()
self.wz_sock.close()
self.sig_sock.close()
