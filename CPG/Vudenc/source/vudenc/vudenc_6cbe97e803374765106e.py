import fnmatch
import inspect
import logging
import os
import random
import re
import string
import tarfile
import threading
import tempfile
import shutil
import subprocess
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from .sosnode import SosNode
from distutils.sysconfig import get_python_lib
from getpass import getpass
from six.moves import input
from textwrap import fill
from soscollector import __version__
"""Main sos-collector class"""
def __init__(self, config):...
os.umask(63)
self.config = config
self.client_list = []
self.node_list = []
self.master = False
self.retrieved = 0
self.need_local_sudo = False
self.clusters = self.config['cluster_types']
if not self.config['list_options']:
def _setup_logging(self):...
if not self.config['tmp_dir']:
self._exit('Exiting on user cancel', 130)
self.logger = logging.getLogger('sos_collector')
self.create_tmp_dir()
self._setup_logging()
self.logger.setLevel(logging.DEBUG)
self.log_debug('Executing %s' % ' '.join(s for s in sys.argv))
self.logfile = tempfile.NamedTemporaryFile(mode='w+', dir=self.config[
    'tmp_dir'], delete=False)
self.log_debug('Found cluster profiles: %s' % self.clusters.keys())
hndlr = logging.StreamHandler(self.logfile)
self.log_debug('Found supported host types: %s' % self.config['host_types']
    .keys())
hndlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
self._parse_options()
hndlr.setLevel(logging.DEBUG)
self.prep()
self.logger.addHandler(hndlr)
console = logging.StreamHandler(sys.stderr)
console.setFormatter(logging.Formatter('%(message)s'))
self.console = logging.getLogger('sos_collector_console')
self.console.setLevel(logging.DEBUG)
self.console_log_file = tempfile.NamedTemporaryFile(mode='w+', dir=self.
    config['tmp_dir'], delete=False)
chandler = logging.StreamHandler(self.console_log_file)
cfmt = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
chandler.setFormatter(cfmt)
self.console.addHandler(chandler)
ui = logging.StreamHandler()
fmt = logging.Formatter('%(message)s')
ui.setFormatter(fmt)
if self.config['verbose']:
ui.setLevel(logging.DEBUG)
ui.setLevel(logging.INFO)
self.console.addHandler(ui)
def _exit(self, msg, error=1):...
"""docstring"""
self.log_error(msg)
self.close_all_connections()
sys.exit(error)
def _parse_options(self):...
"""docstring"""
if self.config['cluster_options']:
for opt in self.config['cluster_options']:
def _validate_option(self, default, cli):...
match = False
"""docstring"""
for option in self.clusters[opt.cluster].options:
if not default.opt_type == bool:
if opt.name == option.name:
if not match:
if not default.opt_type == cli.opt_type:
val = cli.value.lower()
match = True
self._exit('Unknown option provided: %s.%s' % (opt.cluster, opt.name))
msg = 'Invalid option type for %s. Expected %s got %s'
return cli.value
if val not in ['true', 'on', 'false', 'off']:
option.value = self._validate_option(option, opt)
self._exit(msg % (cli.name, default.opt_type, cli.opt_type))
msg = "Invalid value for %s. Accepted values are: 'true', 'false', 'on', 'off'"
if val in ['true', 'on']:
self._exit(msg % cli.name)
return True
return False
def log_info(self, msg):...
"""docstring"""
self.logger.info(msg)
self.console.info(msg)
def log_warn(self, msg):...
"""docstring"""
self.logger.warn(msg)
self.console.warn('WARNING: %s' % msg)
def log_error(self, msg):...
"""docstring"""
self.logger.error(msg)
self.console.error(msg)
def log_debug(self, msg):...
"""docstring"""
caller = inspect.stack()[1][3]
msg = '[sos_collector:%s] %s' % (caller, msg)
self.logger.debug(msg)
if self.config['verbose']:
self.console.debug(msg)
def create_tmp_dir(self):...
"""docstring"""
tmpdir = tempfile.mkdtemp(prefix='sos-collector-', dir='/var/tmp')
self.config['tmp_dir'] = tmpdir
self.config['tmp_dir_created'] = True
def list_options(self):...
"""docstring"""
print("""
The following cluster options are available:
""")
print('{:15} {:15} {:<10} {:10} {:<}'.format('Cluster', 'Option Name',
    'Type', 'Default', 'Description'))
for cluster in self.clusters:
for opt in self.clusters[cluster].options:
print(
    """
Options take the form of cluster.name=value
E.G. "ovirt.no-database=True" or "pacemaker.offline=False\""""
    )
optln = '{:15} {:15} {:<10} {:<10} {:<10}'.format(opt.cluster, opt.name,
    opt.opt_type.__name__, str(opt.value), opt.description)
def delete_tmp_dir(self):...
print(optln)
"""docstring"""
shutil.rmtree(self.config['tmp_dir'])
def _get_archive_name(self):...
"""docstring"""
nstr = 'sos-collector'
if self.config['label']:
nstr += '-%s' % self.config['label']
if self.config['case_id']:
nstr += '-%s' % self.config['case_id']
dt = datetime.strftime(datetime.now(), '%Y-%m-%d')
string.lowercase = string.ascii_lowercase
rand = ''.join(random.choice(string.lowercase) for x in range(5))
return '%s-%s-%s' % (nstr, dt, rand)
