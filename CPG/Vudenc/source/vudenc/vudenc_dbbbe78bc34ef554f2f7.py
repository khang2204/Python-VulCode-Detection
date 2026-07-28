import os
import subprocess
def test_serverextensions():...
"""docstring"""
proc = subprocess.run(['/opt/tljh/user/bin/jupyter-serverextension', 'list',
    '--sys-prefix'], stderr=subprocess.PIPE)
extensions = ['jupyterlab 0.35.3', 'nbgitpuller 0.6.1',
    'nteract_on_jupyter 1.9.12', 'nbresuse ']
for e in extensions:
assert '{} \x1b[32mOK\x1b[0m'.format(e) in proc.stderr.decode()
def test_nbextensions():...
"""docstring"""
proc = subprocess.run(['/opt/tljh/user/bin/jupyter-nbextension', 'list',
    '--sys-prefix'], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
extensions = ['nbresuse/main', 'jupyter-js-widgets/extension']
for e in extensions:
assert '{} \x1b[32m enabled \x1b[0m'.format(e) in proc.stdout.decode()
assert proc.stderr.decode() == '      - Validating: \x1b[32mOK\x1b[0m\n' * len(
    extensions)
def test_labextensions():...
"""docstring"""
assert os.path.exists('/opt/tljh/user/bin/jupyter-labhub')
