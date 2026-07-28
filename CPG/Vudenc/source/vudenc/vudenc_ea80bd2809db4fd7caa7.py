"""
Default Driver for san-stored volumes.

The unique thing about a SAN is that we don't expect that we can run the volume
controller on the SAN hardware.  We expect to access it over SSH or some API.
"""
import random
from eventlet import greenthread
from oslo.config import cfg
from cinder import exception
from cinder.openstack.common import excutils
from cinder.openstack.common import log as logging
from cinder import utils
from cinder.volume import driver
LOG = logging.getLogger(__name__)
san_opts = [cfg.BoolOpt('san_thin_provision', default=True, help=
    'Use thin provisioning for SAN volumes?'), cfg.StrOpt('san_ip', default
    ='', help='IP address of SAN controller'), cfg.StrOpt('san_login',
    default='admin', help='Username for SAN controller'), cfg.StrOpt(
    'san_password', default='', help='Password for SAN controller', secret=
    True), cfg.StrOpt('san_private_key', default='', help=
    'Filename of private key to use for SSH authentication'), cfg.StrOpt(
    'san_clustername', default='', help=
    'Cluster name to use for creating volumes'), cfg.IntOpt('san_ssh_port',
    default=22, help='SSH port to use with SAN'), cfg.BoolOpt(
    'san_is_local', default=False, help=
    'Execute commands locally instead of over SSH; use if the volume service is running on the SAN device'
    ), cfg.IntOpt('ssh_conn_timeout', default=30, help=
    'SSH connection timeout in seconds'), cfg.IntOpt('ssh_min_pool_conn',
    default=1, help='Minimum ssh connections in the pool'), cfg.IntOpt(
    'ssh_max_pool_conn', default=5, help='Maximum ssh connections in the pool')
    ]
CONF = cfg.CONF
CONF.register_opts(san_opts)
"""Base class for SAN-style storage volumes

    A SAN-style storage value is 'different' because the volume controller
    probably won't run on it, so we need to access is over SSH or another
    remote protocol.
    """
def __init__(self, *args, **kwargs):...
execute = kwargs.pop('execute', self.san_execute)
super(SanDriver, self).__init__(*args, execute=execute, **kwargs)
self.configuration.append_config_values(san_opts)
self.run_local = self.configuration.san_is_local
self.sshpool = None
def san_execute(self, *cmd, **kwargs):...
if self.run_local:
return utils.execute(*cmd, **kwargs)
check_exit_code = kwargs.pop('check_exit_code', None)
command = ' '.join(cmd)
return self._run_ssh(command, check_exit_code)
