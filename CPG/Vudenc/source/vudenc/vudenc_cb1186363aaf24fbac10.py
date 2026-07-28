def get_dvd_device(self, dev_dir='/dev'):...
"""docstring"""
patten = '(sr[0-9]|hd[c-z]|cdrom[0-9]?)'
for dvd in [re.match(patten, dev) for dev in os.listdir(dev_dir)]:
if dvd is not None:
return '/dev/{0}'.format(dvd.group(0))
