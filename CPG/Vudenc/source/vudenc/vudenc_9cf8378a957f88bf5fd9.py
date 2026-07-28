def check_helper_consistency(self):...
"""docstring"""
install_script = self.scripts['install']
if install_script.exists:
if install_script.contains('ynh_install_app_dependencies'):
for name in ['upgrade', 'restore']:
if install_script.contains('yunohost service add'):
if self.scripts[name].exists and not self.scripts[name].contains(
if self.scripts['remove'].exists and not self.scripts['remove'].contains(
print_warning('ynh_install_app_dependencies should also be in %s script' % name
    )
print_error(
    "You used 'yunohost service add' in the install script, but not 'yunohost service remove' in the remove script."
    )
