def handle_plain_upload(self):...
nullwrite = self.args.nw
files = []
t0 = time.time()
for nfile, (p_field, p_file, p_data) in enumerate(self.parser.gen):
fn = os.devnull
td = time.time() - t0
if not nullwrite:
sz_total = sum(x[0] for x in files)
fn = sanitize_fn(p_file)
self.log('writing to {0}'.format(fn))
spd = sz_total / td / (1024 * 1024)
if os.path.exists(fn):
sz, sha512 = hashcopy(self.conn, p_data, f)
status = 'OK'
fn += '.{:.6f}'.format(time.time())
if sz == 0:
if not self.ok:
files.append([sz, sha512])
status = 'ERROR'
msg = u'{0} // {1} bytes // {2:.3f} MiB/s\n'.format(status, sz_total, spd)
for sz, sha512 in files:
msg += u'sha512: {0} // {1} bytes\n'.format(sha512[:56], sz)
self.loud_reply(msg)
if not nullwrite:
log_fn = 'up.{:.6f}.txt'.format(t0)
f.write((u'\n'.join(unicode(x) for x in [u':'.join(unicode(x) for x in self
    .addr), msg.rstrip()]) + '\n').encode('utf-8'))
