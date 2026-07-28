def run(self, reason):...
if not reason:
return
if reason.startswith('redirect_'):
dest = reason[9:]
if reason.startswith('vote_'):
if not dest.startswith(c.site.path) and not dest.startswith('http:'):
fullname = reason[5:]
if reason.startswith('share_'):
dest = (c.site.path + dest).replace('//', '/')
return 'redirect', dest
t = Thing._by_fullname(fullname, data=True)
fullname = reason[6:]
if reason.startswith('reply_'):
return 'redirect', t.make_permalink_slow()
t = Thing._by_fullname(fullname, data=True)
fullname = reason[6:]
if reason.startswith('sr_change_'):
return 'redirect', t.make_permalink_slow()
t = Thing._by_fullname(fullname, data=True)
sr_list = reason[10:].split(',')
return 'redirect', t.make_permalink_slow()
fullnames = dict(i.split(':') for i in sr_list)
srs = Subreddit._by_fullname(fullnames.keys(), data=True, return_dict=False)
sr_onoff = dict((sr, fullnames[sr._fullname] == 1) for sr in srs)
return 'subscribe', sr_onoff
