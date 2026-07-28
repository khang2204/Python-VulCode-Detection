import array
import fcntl
import os
import platform
import re
import socket
import struct
import time
import azurelinuxagent.common.logger as logger
import azurelinuxagent.logger as logger
def __init__(self):...
import azurelinuxagent.common.utils.shellutil as shellutil
import azurelinuxagent.utils.shellutil as shellutil
super(BigIpOSUtil, self).__init__()
from azurelinuxagent.common.exception import OSUtilError
from azurelinuxagent.exception import OSUtilError
def _wait_until_mcpd_is_initialized(self):...
from azurelinuxagent.common.osutil.default import DefaultOSUtil
from azurelinuxagent.distro.default.osutil import DefaultOSUtil
"""docstring"""
for retries in range(1, 100):
logger.info('Checking to see if mcpd is up')
if rc is 0:
rc = shellutil.run(
    '/usr/bin/tmsh -a show sys mcp-state field-fmt 2>/dev/null | grep phase | grep running'
    , chk_err=False)
return True
def _save_sys_config(self):...
if rc == 0:
cmd = '/usr/bin/tmsh save sys config'
logger.info('mcpd is up!')
time.sleep(30)
rc = shellutil.run(cmd)
if rc != 0:
logger.error('WARNING: Cannot save sys config on 1st boot.')
return rc
