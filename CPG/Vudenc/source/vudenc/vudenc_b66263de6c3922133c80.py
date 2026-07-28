def create_spawn(proxy, proxytype, pc, uq=None):...
for domain in domains:
if domain in targets:
tlist = targets[domain]
tlist = list()
if domain in forums:
targets[domain] = tlist
fset = forums[domain]
fset = set()
net = make_net(proxy, proxytype)
forums[domain] = fset
net.cookiefname = (proxy if proxy else 'noproxy') + '_' + domain
w = UniWipe(fset, tlist, sbjfun, message, pc, net, domain, Mailinator, uq(
    domain) if uq else None)
w.stoponclose = c.stop_on_closed
w.die_on_neterror = c.die_on_neterror
w.caprate_minp = c.caprate_minp
w.caprate_limit = c.caprate_limit
w.conlimit = c.conlimit
w.comment_successtimeout = 0.2
if c.upload_avatar:
w.hooks['post_login'].append(upload_avatar)
yield w
