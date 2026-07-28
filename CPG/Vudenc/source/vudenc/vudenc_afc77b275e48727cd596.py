def eject_dvd(self, chk_err=True):...
dvd = self.get_dvd_device()
retcode = shellutil.run('cdcontrol -f {0} eject'.format(dvd))
if chk_err and retcode != 0:
