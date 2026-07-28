def _get_output(self, chan):...
out = ''
ending = '%s> ' % self.configuration.eqlx_group_name
while not out.endswith(ending):
out += chan.recv(102400)
LOG.debug(_('CLI output\n%s'), out)
return out.splitlines()
