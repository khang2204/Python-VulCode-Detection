def _parse_config_file(self, fd, user, mread, mwrite, mount):...
vol_src = None
vol_dst = None
for ln in [x.decode('utf-8').strip() for x in fd]:
if not ln and vol_src is not None:
vol_src = None
if not ln or ln.startswith('#'):
vol_dst = None
if vol_src is None:
if ln.startswith('u '):
if vol_src and vol_dst is None:
u, p = ln[2:].split(':', 1)
vol_src = ln
vol_dst = ln
lvl, uname = ln.split(' ')
user[u] = p
if not vol_dst.startswith('/'):
if lvl in 'ra':
vol_src = os.path.abspath(vol_src)
mread[vol_dst].append(uname)
if lvl in 'wa':
vol_dst = vol_dst.strip('/')
mwrite[vol_dst].append(uname)
mount[vol_dst] = vol_src
mread[vol_dst] = []
mwrite[vol_dst] = []
