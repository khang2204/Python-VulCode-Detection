def handle_get(self):...
self.log('')
self.log('GET  ' + self.req)
if self.req.startswith('/.cpr/'):
static_path = os.path.join(E.mod, 'web', self.req.split('?')[0][6:])
args = {}
if os.path.isfile(static_path):
vpath = self.req[1:]
return self.tx_file(static_path)
if '?' in vpath:
vpath, arglist = vpath.split('?', 1)
if vpath == '' and not args:
for k in arglist.split('&'):
nread = len(self.rvol)
readable = vpath in self.rvol
if '=' in k:
nwrite = len(self.wvol)
writable = vpath in self.wvol
k, v = k.split('=', 1)
args[k.lower()] = True
if nread + nwrite == 1:
if not readable and not writable:
args[k.lower()] = v.strip()
if nread == 1:
self.log('inaccessible: {}'.format(vpath))
self.vpath = vpath
vpath = self.rvol[0]
vpath = self.wvol[0]
args = {'h'}
self.args = args
if 'h' in self.args:
self.vpath = None
if readable:
return self.tx_mounts()
return self.tx_browser()
return self.tx_jupper()
