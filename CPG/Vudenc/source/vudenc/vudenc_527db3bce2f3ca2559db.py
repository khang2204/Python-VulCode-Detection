import azurelinuxagent.common.utils.fileutil as fileutil
import azurelinuxagent.common.utils.shellutil as shellutil
import azurelinuxagent.common.utils.textutil as textutil
import azurelinuxagent.common.logger as logger
from azurelinuxagent.common.exception import OSUtilError
from azurelinuxagent.common.osutil.default import DefaultOSUtil
from azurelinuxagent.common.future import ustr
def __init__(self):...
super(FreeBSDOSUtil, self).__init__()
self._scsi_disks_timeout_set = False
def set_hostname(self, hostname):...
rc_file_path = '/etc/rc.conf'
conf_file = fileutil.read_file(rc_file_path).split('\n')
textutil.set_ini_config(conf_file, 'hostname', hostname)
fileutil.write_file(rc_file_path, '\n'.join(conf_file))
shellutil.run('hostname {0}'.format(hostname), chk_err=False)
def restart_ssh_service(self):...
return shellutil.run('service sshd restart', chk_err=False)
