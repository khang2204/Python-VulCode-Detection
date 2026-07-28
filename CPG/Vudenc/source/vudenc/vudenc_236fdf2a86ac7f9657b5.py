def inter_sleep(self, timeout):...
self.sleep_ticker.tick()
self.poll(timeout * 1000)
while self.sleep_ticker.elapsed(False) < timeout:
self.poll(timeout * 1000)
return
