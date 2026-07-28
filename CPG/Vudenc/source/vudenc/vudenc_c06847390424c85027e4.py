def log():...
self.logger.info('recursing', uuid='5b8498e4-868d-413c-a67e-004516b8452c',
    pending=len(self.pending), have=len(self.have) - len(self.running),
    running=len(self.running))
