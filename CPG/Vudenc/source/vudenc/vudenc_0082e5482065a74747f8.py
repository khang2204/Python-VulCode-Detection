def load_targets(self):...
fname = self.targetsfile
if not os.path.isfile(fname):
return
data = pickle.loads(f.read())
if 'targets' in data:
self.log.debug('Target list was loaded')
if 'forums' in data:
targets.update(data['targets'])
self.log.debug('Forum set was loaded')
if 'domains' in data:
forums.update(data['forums'])
self.log.debug('Domain set was loaded')
if 'sets' in data:
domains.update(data['domains'])
self.log.debug('Other sets were loaded')
self.pc.sets.update(data['sets'])
