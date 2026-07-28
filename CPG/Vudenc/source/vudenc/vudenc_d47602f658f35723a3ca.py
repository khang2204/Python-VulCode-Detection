def add_target(domain, id_, tuser=None):...
if domain not in targets:
targets[domain] = []
tlist = targets[domain]
id_ = str(id_)
tuser = tuser or ''
t = tuser, id_
logger.info('Appending %s to targets[%s]', repr(t), domain)
tlist.append(t)
