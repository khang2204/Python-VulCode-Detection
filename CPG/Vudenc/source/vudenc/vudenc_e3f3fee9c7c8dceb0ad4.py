def start(self, ctx, sig_addr, *args, **kvargs):...
self.ctx = ctx
self.sig_addr = sig_addr
threading.Thread.start(self, *args, **kvargs)
