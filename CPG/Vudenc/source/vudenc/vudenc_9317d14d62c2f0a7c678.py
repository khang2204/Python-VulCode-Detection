def gometalinter(self):...
"""docstring"""
args = shlex.split('{0} {1}'.format(self.binary, self.options), posix=os.
    name != 'nt')
gometalinter = spawn(args, stdout=PIPE, stderr=PIPE, env=self.env)
out, err = gometalinter.communicate()
if err is not None and len(err) > 0:
if sys.version_info >= (3,):
if sys.version_info >= (3,):
err = err.decode('utf8')
out = out.decode('utf8')
return self._normalize(json.loads(out))
