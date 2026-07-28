from jupyter_core.paths import jupyter_data_dir
import subprocess
import os
PEM_FILE = os.path.join(jupyter_data_dir(), 'notebook.pem')
c = get_config()
c.NotebookApp.ip = os.getenv('INTERFACE', '') or '*'
c.NotebookApp.port = int(os.getenv('PORT', '') or 8888)
c.NotebookApp.open_browser = False
if 'USE_HTTPS' in os.environ:
if not os.path.isfile(PEM_FILE):
if 'PASSWORD' in os.environ:
subprocess.check_call(['openssl', 'req', '-new', '-newkey', 'rsa:2048',
    '-days', '365', '-nodes', '-x509', '-subj',
    '/C=XX/ST=XX/L=XX/O=generated/CN=generated', '-keyout', PEM_FILE,
    '-out', PEM_FILE])
c.NotebookApp.certfile = PEM_FILE
from IPython.lib import passwd
c.NotebookApp.password = passwd(os.environ['PASSWORD'])
