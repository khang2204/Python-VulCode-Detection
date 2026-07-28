"""Volume driver for Dell EqualLogic Storage."""
import functools
import random
import eventlet
from eventlet import greenthread
import greenlet
from oslo.config import cfg
from cinder import exception
from cinder.openstack.common import excutils
from cinder.openstack.common import log as logging
from cinder.openstack.common import processutils
from cinder import utils
from cinder.volume.drivers.san import SanISCSIDriver
LOG = logging.getLogger(__name__)
eqlx_opts = [cfg.StrOpt('eqlx_group_name', default='group-0', help=
    'Group name to use for creating volumes'), cfg.IntOpt(
    'eqlx_cli_timeout', default=30, help=
    'Timeout for the Group Manager cli command execution'), cfg.IntOpt(
    'eqlx_cli_max_retries', default=5, help=
    'Maximum retry count for reconnection'), cfg.BoolOpt('eqlx_use_chap',
    default=False, help='Use CHAP authentication for targets?'), cfg.StrOpt
    ('eqlx_chap_login', default='admin', help='Existing CHAP account name'),
    cfg.StrOpt('eqlx_chap_password', default='password', help=
    'Password for specified CHAP account name', secret=True), cfg.StrOpt(
    'eqlx_pool', default='default', help=
    'Pool in which volumes will be created')]
CONF = cfg.CONF
CONF.register_opts(eqlx_opts)
def with_timeout(f):...
@functools.wraps(f)...
timeout = kwargs.pop('timeout', None)
gt = eventlet.spawn(f, self, *args, **kwargs)
if timeout is None:
return gt.wait()
kill_thread = eventlet.spawn_after(timeout, gt.kill)
res = gt.wait()
kill_thread.cancel()
return __inner
return res
