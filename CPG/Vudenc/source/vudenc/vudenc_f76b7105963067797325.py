def _fmt_output(self, stdout=None, stderr=None, rc=0):...
"""docstring"""
if isinstance(stdout, (six.string_types, bytes)):
stdout = [stdout.decode('utf-8')]
if isinstance(stderr, (six.string_types, bytes)):
stderr = [stderr.decode('utf-8')]
if stdout:
stdout = ''.join(s for s in stdout) or True
if stderr:
stderr = ' '.join(s for s in stderr) or False
res = {'status': rc, 'stdout': stdout, 'stderr': stderr}
return res
