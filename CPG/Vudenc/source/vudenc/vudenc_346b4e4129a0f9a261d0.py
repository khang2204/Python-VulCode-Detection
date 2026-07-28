def _determine_ssh_error(self, errors):...
"""docstring"""
for err in errors:
errno = errors[err].errno
return None
if errno == 103:
return 'Key exchange failed'
if errno == 108:
return 'SSH version is unsupported'
if errno == 111:
return 'Could not open SSH session on port %s' % self.config['ssh_port']
if errno == 115:
return "No valid SSH user '%s'" % self.config['ssh_user']
