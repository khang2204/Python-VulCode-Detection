def determine_sos_label(self):...
"""docstring"""
label = ''
label += self.config['cluster'].get_node_label(self)
if self.config['label']:
label += '%s' % self.config['label'] if not label else '-%s' % self.config[
    'label']
if not label:
return None
self.log_debug('Label for sosreport set to %s' % label)
if self.check_sos_version('3.6'):
lcmd = '--label'
lcmd = '--name'
return '%s=%s' % (lcmd, label)
label = '%s-%s' % (self.address.split('.')[0], label)
