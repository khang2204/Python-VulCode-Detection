def forumwipe_loop(self):...
for f in self.forums:
self.counter_tick()
self.addtopic(self.msgfun(), self.sbjfun(), f)
self.counters['topics'] += 1
self.w.sleep(self.topic_successtimeout)
self.topic_successtimeout = self.topic_successtimeout + 0.1
self.log.info('Wait5Min exc caught, topic_successtimeout + 0.1, cur: %f',
    self.topic_successtimeout)
self.w.sleep(self.topic_successtimeout)
self.log.error('Too many wrong answers to CAPTCHA')
self.long_sleep(10)
self.log.warning('%s: %s', e, e.answer)
self.w.sleep(self.errortimeout)
self.log.error(e)
self.w.sleep(self.errortimeout)
self.log.warn(e)
self.w.sleep(self.errortimeout)
