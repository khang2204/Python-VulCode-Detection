def _format_cmd(self, cmd):...
"""docstring"""
if self.config['become_root']:
return "su -c '%s'" % cmd
if self.config['need_sudo']:
return 'sudo -S %s' % cmd
return cmd
