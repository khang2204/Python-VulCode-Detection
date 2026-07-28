def check_helper_usage_dependencies(self):...
"""docstring"""
if self.contains('ynh_package_install') or self.contains('apt-get install'):
print_warning(
    'You should not use `ynh_package_install` or `apt-get install`, use `ynh_install_app_dependencies` instead'
    )
if self.contains('ynh_package_remove') or self.contains('apt-get remove'):
print_warning(
    'You should not use `ynh_package_remove` or `apt-get remove`, use `ynh_remove_app_dependencies` instead'
    )
