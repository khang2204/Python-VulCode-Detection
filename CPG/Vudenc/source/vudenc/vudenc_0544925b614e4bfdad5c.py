def connect(self, reschedule_on_err=True):...
self._logger.info('Will connect to events endpoint')
self.reply = self.get(self.request)
self.reply.readyRead.connect(self.on_read_data)
self.reply.error.connect(lambda error: self.on_error(error,
    reschedule_on_err=reschedule_on_err))
