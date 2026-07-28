def parse_config(self):...
for k in self.args:
if self.args[k]:
if self['sos_opt_line']:
self[k] = self.args[k]
self['sos_opt_line'] = pipes.quote(self['sos_opt_line'])
