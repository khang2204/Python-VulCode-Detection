import inspect
import os
import pipes
import re
import six
import socket
import sys
""" Dict subclass that is used to handle configuration information
    needed by both SosCollector and the SosNode classes """
def __init__(self, args=None):...
self.args = args
self.set_defaults()
self.parse_config()
self.parse_options()
self.check_user_privs()
self.parse_node_strings()
self['host_types'] = self._load_supported_hosts()
self['cluster_types'] = self._load_clusters()
def set_defaults(self):...
self['sos_mod'] = {}
self['master'] = ''
self['strip_sos_path'] = ''
self['ssh_port'] = 22
self['ssh_user'] = 'root'
self['sos_cmd'] = 'sosreport --batch'
self['no_local'] = False
self['tmp_dir'] = None
self['out_dir'] = '/var/tmp/'
self['nodes'] = None
self['debug'] = False
self['tmp_dir_created'] = False
self['cluster_type'] = None
self['cluster'] = None
self['password'] = False
self['label'] = None
self['case_id'] = None
self['timeout'] = 300
self['all_logs'] = False
self['alloptions'] = False
self['no_pkg_check'] = False
self['hostname'] = socket.gethostname()
ips = [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)]
self['ip_addrs'] = list(set(ips))
self['cluster_options'] = []
self['image'] = None
self['skip_plugins'] = []
self['enable_plugins'] = []
self['plugin_options'] = []
self['only_plugins'] = []
self['list_options'] = False
self['hostlen'] = len(self['master']) or len(self['hostname'])
self['need_sudo'] = False
self['sudo_pw'] = ''
self['become_root'] = False
self['root_password'] = ''
self['threads'] = 4
self['compression'] = ''
self['verify'] = False
self['chroot'] = ''
self['sysroot'] = ''
self['sos_opt_line'] = ''
self['batch'] = False
self['verbose'] = False
self['preset'] = ''
self['insecure_sudo'] = False
self['log_size'] = 0
self['host_types'] = []
def parse_node_strings(self):...
"""docstring"""
if not self['nodes']:
return
nodes = []
if not isinstance(self['nodes'], list):
self['nodes'] = [self['nodes']]
for node in self['nodes']:
idxs = [i for i, m in enumerate(node) if m == ',']
self['nodes'] = nodes
idxs.append(len(node))
def parse_config(self):...
start = 0
for k in self.args:
pos = 0
if self.args[k]:
if self['sos_opt_line']:
for idx in idxs:
self[k] = self.args[k]
self['sos_opt_line'] = pipes.quote(self['sos_opt_line'])
def parse_cluster_options(self):...
if pos != len(node):
pos = idx
opts = []
nodes.append(node[pos + 1:])
reg = node[start:idx]
if not isinstance(self['cluster_options'], list):
re.compile(re.escape(reg))
self['cluster_options'] = [self['cluster_options']]
if self['cluster_options']:
if '[' in reg and ']' not in reg:
for option in self['cluster_options']:
self['cluster_options'] = opts
nodes.append(reg.lstrip(','))
cluster = option.split('.')[0]
def parse_options(self):...
start = idx
name = option.split('.')[1].split('=')[0]
self.parse_cluster_options()
value = pipes.quote(option.split('=')[1].split()[0])
value = 'True'
opts.append(ClusterOption(name, value, value.__class__, cluster))
for opt in ['skip_plugins', 'enable_plugins', 'plugin_options', 'only_plugins'
if self[opt]:
def check_user_privs(self):...
opts = []
if not self['ssh_user'] == 'root':
if isinstance(self[opt], six.string_types):
self['need_sudo'] = True
def _import_modules(self, modname):...
self[opt] = [self[opt]]
for option in self[opt]:
"""docstring"""
opts += option.split(',')
self[opt] = opts
mod_short_name = modname.split('.')[2]
module = __import__(modname, globals(), locals(), [mod_short_name])
modules = inspect.getmembers(module, inspect.isclass)
for mod in modules:
if mod[0] in ('SosHost', 'Cluster'):
return modules
modules.remove(mod)
