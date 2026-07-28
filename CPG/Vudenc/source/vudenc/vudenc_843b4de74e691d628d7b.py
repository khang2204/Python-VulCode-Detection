from sup.net import NetError
from wzworkers import WorkerInterrupt
from wipeskel import WipeSkel, WipeState, cstate
from beon import exc, regexp
import re
def __init__(self, forums, targets, sbjfun, msgfun, *args, **kvargs):...
self.sbjfun = sbjfun
self.msgfun = msgfun
self.forums = forums
self.targets = type(targets) == str and [('', targets)] or type(targets
    ) == tuple and list(targets) or targets
super().__init__(*args, **kvargs)
def on_caprate_limit(self, rate):...
if not self.logined:
self._capdata = 0, 0
self.log.warning('Caprate limit reached, calling dologin() for now')
return
self.dologin()
def comment_loop(self):...
for t in self.targets:
self.schedule(self.add_comment, (t, self.msgfun()))
if len(self.targets) == 0:
self.schedule(self.scan_targets_loop)
self.schedule(self.comment_loop)
def add_comment(self, t, msg):...
if True:
def forumwipe_loop(self):...
self.postmsg(t[1], msg, t[0])
self.counters['comments'] += 1
for f in self.forums:
self.w.sleep(self.comment_successtimeout)
self.counter_tick()
def get_targets(self):...
self.w.sleep(self.comment_successtimeout)
self.addtopic(self.msgfun(), self.sbjfun(), f)
self.counters['topics'] += 1
found_count = 0
self.schedule(self.add_comment, (t, msg))
self.w.sleep(self.topic_successtimeout)
for user, forum in self.forums:
self.targets.remove(t)
self.w.sleep(self.comment_successtimeout)
self.topic_successtimeout = self.topic_successtimeout + 0.1
targets = []
return found_count
self.log.error('Too many wrong answers to CAPTCHA')
self.log.info('Wait5Min exc caught, topic_successtimeout + 0.1, cur: %f',
    self.topic_successtimeout)
self.log.debug('Scanning first page of the forum %s:%s', user, forum)
self.schedule(self.add_comment, (t, msg))
self.w.sleep(self.topic_successtimeout)
page = self.site.get_page('1', forum, user)
self.log.warn('%s: %s', e, e.answer)
self.log.error('Too many wrong answers to CAPTCHA')
rxp = re.compile(regexp.f_sub_id.format(user, self.site.domain, forum))
self.schedule(self.add_comment, (t, msg))
self.long_sleep(10)
found = set(map(lambda x: (user, x[0] + x[1]), rxp.findall(page)))
self.schedule(self.add_comment, (t, msg))
self.log.warning('%s: %s', e, e.answer)
for t in found:
self.schedule_first(self.switch_user)
self.w.sleep(self.errortimeout)
if t in self.pc.sets['closed'] or t in self.pc.sets['bumplimit'
lt = len(targets)
self.log.info('Removing %s from targets', t)
self.log.error(e)
targets.append(t)
found_count += lt
self.targets.remove(t)
self.w.sleep(self.errortimeout)
self.w.sleep(self.errortimeout)
if lt > 0:
self.schedule(self.add_comment, (t, msg))
self.log.warn(e)
self.log.info('Found %d new targets in forum %s:%s', lt, user, forum)
self.log.debug('Found no new targets in forum %s:%s', user, forum)
self.w.sleep(self.errortimeout)
self.w.sleep(self.errortimeout)
self.targets.extend(targets)
self.targets.remove(t)
self.w.sleep(self.errortimeout)
self.log.exception(e)
self.w.sleep(self.errortimeout)
