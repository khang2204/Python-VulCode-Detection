def add_target_exc(domain, id_, tuser=None):...
if domain not in targets:
targets[domain] = []
tlist = targets[domain]
id_ = str(id_)
tuser = tuser or ''
t = tuser, id_
if t in protected:
if t not in tlist:
logger.info('Appending %s to targets[%s]', repr(t), domain)
tlist.append(t)
