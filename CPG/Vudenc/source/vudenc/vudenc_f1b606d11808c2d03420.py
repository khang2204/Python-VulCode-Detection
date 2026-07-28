def configure_sos_cmd(self):...
"""docstring"""
if self.config['sos_opt_line']:
filt = ['&', '|', '>', '<']
if self.config['case_id']:
if any(f in self.config['sos_opt_line'] for f in filt):
self.config['sos_cmd'] += ' --case-id=%s' % self.config['case_id']
if self.config['alloptions']:
self.log_warn(
    'Possible shell script found in provided sos command. Ignoring --sos-cmd option entirely.'
    )
self.config['sos_cmd'] = '%s %s' % (self.config['sos_cmd'], self.config[
    'sos_opt_line'])
self.config['sos_cmd'] += ' --alloptions'
if self.config['verify']:
self.config['sos_opt_line'] = None
self.log_debug('User specified manual sosreport command. Command set to %s' %
    self.config['sos_cmd'])
self.config['sos_cmd'] += ' --verify'
if self.config['log_size']:
return True
self.config['sos_cmd'] += ' --log-size=%s' % self.config['log_size']
if self.config['sysroot']:
self.config['sos_cmd'] += ' -s %s' % self.config['sysroot']
if self.config['chroot']:
self.config['sos_cmd'] += ' -c %s' % self.config['chroot']
if self.config['compression']:
self.config['sos_cmd'] += ' -z %s' % self.config['compression']
self.log_debug('Initial sos cmd set to %s' % self.config['sos_cmd'])
