def prep(self):...
"""docstring"""
disclaimer = """This utility is used to collect sosreports from multiple nodes simultaneously. It uses the python-paramiko library to manage the SSH connections to remote systems. If this library is not acceptable for use in your environment, you should not use this utility.

An archive of sosreport tarballs collected from the nodes will be generated in %s and may be provided to an appropriate support representative.

The generated archive may contain data considered sensitive and its content should be reviewed by the originating organization before being passed to any third party.

No configuration changes will be made to the system running this utility or remote systems that it connects to.
"""
self.console.info("""
sos-collector (version %s)
""" % __version__)
intro_msg = self._fmt_msg(disclaimer % self.config['tmp_dir'])
self.console.info(intro_msg)
prompt = """
Press ENTER to continue, or CTRL-C to quit
"""
if not self.config['batch']:
input(prompt)
if not self.config['password']:
self.log_debug('password not specified, assuming SSH keys')
if self.config['password']:
msg = """sos-collector ASSUMES that SSH keys are installed on all nodes unless the --password option is provided.
"""
self.log_debug('password specified, not using SSH keys')
if self.config['need_sudo'] and not self.config['insecure_sudo']:
self.console.info(self._fmt_msg(msg))
msg = 'Provide the SSH password for user %s: ' % self.config['ssh_user']
if not self.config['password']:
if self.config['become_root']:
self.config['password'] = getpass(prompt=msg)
self.log_debug('non-root user specified, will request sudo password')
if not self.config['insecure_sudo']:
if not self.config['ssh_user'] == 'root':
if self.config['master']:
msg = (
    'A non-root user has been provided. Provide sudo password for %s on remote nodes: '
     % self.config['ssh_user'])
self.config['sudo_pw'] = self.config['password']
self.log_debug('non-root user asking to become root remotely')
self.log_info(
    'Option to become root but ssh user is root. Ignoring request to change user on node'
    )
self.connect_to_master()
self.master = SosNode('localhost', self.config)
self.log_debug('Unable to determine local installation: %s' % err)
if self.config['cluster_type']:
self.config['sudo_pw'] = getpass(prompt=msg)
msg = ('User %s will attempt to become root. Provide root password: ' %
    self.config['ssh_user'])
self.config['become_root'] = False
self.config['no_local'] = True
self._exit(
    """Unable to determine local installation. Use the --no-local option if localhost should not be included.
Aborting...
"""
    , 1)
self.config['cluster'] = self.clusters[self.config['cluster_type']]
self.determine_cluster()
self.config['root_password'] = getpass(prompt=msg)
self.config['cluster'].master = self.master
if self.config['cluster'] is None and not self.config['nodes']:
self.config['need_sudo'] = False
msg = """Cluster type could not be determined and no nodes provided
Aborting..."""
if self.config['cluster']:
self._exit(msg, 1)
self.config['cluster'].setup()
self.get_nodes()
self.config['cluster'].modify_sos_cmd()
self.intro()
self.configure_sos_cmd()
