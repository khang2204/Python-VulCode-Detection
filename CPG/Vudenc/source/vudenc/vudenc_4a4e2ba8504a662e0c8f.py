def remove_target(domain, id_, tuser=None):...
tlist = targets[domain]
id_ = str(id_)
tuser = tuser or ''
t = tuser, id_
logger.info('Removing %s from targets[%s]', repr(t), domain)
tlist.remove(t)
