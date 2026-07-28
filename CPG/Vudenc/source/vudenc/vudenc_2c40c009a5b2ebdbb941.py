def _install_linters(self):...
"""docstring"""
args = shlex.split('{0} --install'.format(self.binary))
gometalinter = spawn(args, stdout=PIPE, stderr=PIPE, env=self.env)
_, err = gometalinter.communicate()
if err is not None and len(err) > 0:
if sys.version_info >= (3,):
err = err.decode('utf8')
