def check_verifications_done_before_modifying_system(self):...
"""docstring"""
if not self.contains('ynh_die') and not self.contains('exit'):
return
modifying_cmds = ('cp', 'mkdir', 'rm', 'chown', 'chmod', 'apt-get', 'apt',
    'service', 'find', 'sed', 'mysql', 'swapon', 'mount', 'dd', 'mkswap',
    'useradd')
cmds_before_exit = []
for cmd in self.lines:
cmd = ' '.join(cmd)
for modifying_cmd in modifying_cmds:
if 'ynh_die' in cmd or 'exit' in cmd:
if any(modifying_cmd in cmd for cmd in cmds_before_exit):
cmds_before_exit.append(cmd)
print_error(
    """[YEP-2.4] 'ynh_die' or 'exit' command is executed with system modification before (cmd '%s').
This system modification is an issue if a verification exit the script.
You should move this verification before any system modification."""
     % modifying_cmd, False)
return
