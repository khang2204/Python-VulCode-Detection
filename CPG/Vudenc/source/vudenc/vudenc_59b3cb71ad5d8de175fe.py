"""
HP Lefthand SAN ISCSI Driver.

The driver communicates to the backend aka Cliq via SSH to perform all the
operations on the SAN.
"""
from lxml import etree
from cinder import exception
from cinder.openstack.common import log as logging
from cinder.volume.drivers.san.san import SanISCSIDriver
LOG = logging.getLogger(__name__)
"""Executes commands relating to HP/Lefthand SAN ISCSI volumes.

    We use the CLIQ interface, over SSH.

    Rough overview of CLIQ commands used:

    :createVolume:    (creates the volume)

    :getVolumeInfo:    (to discover the IQN etc)

    :getClusterInfo:    (to discover the iSCSI target IP address)

    :assignVolumeChap:    (exports it with CHAP security)

    The 'trick' here is that the HP SAN enforces security by default, so
    normally a volume mount would need both to configure the SAN in the volume
    layer and do the mount on the compute layer.  Multi-layer operations are
    not catered for at the moment in the cinder architecture, so instead we
    share the volume using CHAP at volume creation time.  Then the mount need
    only use those CHAP credentials, so can take place exclusively in the
    compute layer.
    """
device_stats = {}
def __init__(self, *args, **kwargs):...
super(HpSanISCSIDriver, self).__init__(*args, **kwargs)
self.cluster_vip = None
def _cliq_run(self, verb, cliq_args, check_exit_code=True):...
"""docstring"""
cliq_arg_strings = []
for k, v in cliq_args.items():
cliq_arg_strings.append(' %s=%s' % (k, v))
cmd = verb + ''.join(cliq_arg_strings)
return self._run_ssh(cmd, check_exit_code)
