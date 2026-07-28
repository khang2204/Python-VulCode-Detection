def set_scsi_disks_timeout(self, timeout):...
if self._scsi_disks_timeout_set:
return
ret, output = shellutil.run_get_output('sysctl kern.cam.da.default_timeout={0}'
    .format(timeout))
if ret:
self._scsi_disks_timeout_set = True
