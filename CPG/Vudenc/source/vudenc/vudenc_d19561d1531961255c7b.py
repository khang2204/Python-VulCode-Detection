def test_nbextensions():...
"""docstring"""
proc = subprocess.run(['/opt/tljh/user/bin/jupyter-nbextension', 'list',
    '--sys-prefix'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
extensions = ['nbresuse/main', 'jupyter-js-widgets/extension']
for e in extensions:
assert '{} \x1b[32m enabled \x1b[0m'.format(e) in proc.stdout.decode()
assert proc.stderr.decode() == '      - Validating: \x1b[32mOK\x1b[0m\n' * len(
    extensions)
