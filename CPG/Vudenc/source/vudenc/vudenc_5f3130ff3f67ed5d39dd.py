def intro(self):...
"""docstring"""
self.console.info('')
if not self.node_list and not self.master.connected:
self._exit(
    """No nodes were detected, or nodes do not have sos installed.
Aborting..."""
    )
self.console.info('The following is a list of nodes to collect from:')
if self.master.connected:
self.console.info('\t%-*s' % (self.config['hostlen'], self.config['master']))
for node in sorted(self.node_list):
self.console.info('\t%-*s' % (self.config['hostlen'], node))
self.console.info('')
if not self.config['case_id'] and not self.config['batch']:
msg = 'Please enter the case id you are collecting reports for: '
self.config['case_id'] = input(msg)
