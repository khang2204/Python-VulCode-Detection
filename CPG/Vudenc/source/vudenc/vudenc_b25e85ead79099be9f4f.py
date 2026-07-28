"""
Volume driver for HP 3PAR Storage array.
This driver requires 3.1.2 MU2 firmware on the 3PAR array.

You will need to install the python hp3parclient.
sudo pip install hp3parclient

Set the following in the cinder.conf file to enable the
3PAR iSCSI Driver along with the required flags:

volume_driver=cinder.volume.drivers.san.hp.hp_3par_iscsi.HP3PARISCSIDriver
"""
import sys
from hp3parclient import exceptions as hpexceptions
from cinder import exception
from cinder.openstack.common import log as logging
from cinder import utils
import cinder.volume.driver
from cinder.volume.drivers.san.hp import hp_3par_common as hpcommon
from cinder.volume.drivers.san import san
VERSION = 1.1
LOG = logging.getLogger(__name__)
DEFAULT_ISCSI_PORT = 3260
"""OpenStack iSCSI driver to enable 3PAR storage array.

    Version history:
        1.0 - Initial driver
        1.1 - QoS, extend volume, multiple iscsi ports, remove domain,
              session changes, faster clone, requires 3.1.2 MU2 firmware.

    """
def __init__(self, *args, **kwargs):...
super(HP3PARISCSIDriver, self).__init__(*args, **kwargs)
self.common = None
self.configuration.append_config_values(hpcommon.hp3par_opts)
self.configuration.append_config_values(san.san_opts)
def _init_common(self):...
return hpcommon.HP3PARCommon(self.configuration)
