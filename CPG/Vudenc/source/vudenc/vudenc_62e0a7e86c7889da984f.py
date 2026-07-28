def check_deprecated_practices(self):...
if self.contains('yunohost app setting'):
print_warning(
    "'yunohost app setting' shouldn't be used directly. Please use 'ynh_app_setting_(set,get,delete)' instead."
    )
if self.contains('yunohost app checkurl'):
print_warning(
    "'yunohost app checkurl' is deprecated. Please use 'ynh_webpath_register' instead."
    )
if self.contains('yunohost app checkport'):
print_warning(
    "'yunohost app checkport' is deprecated. Please use 'ynh_find_port' instead."
    )
if self.contains('yunohost app initdb'):
print_warning(
    "'yunohost app initdb' is deprecated. Please use 'ynh_mysql_setup_db' instead."
    )
if self.contains('exit'):
print_warning("'exit' command shouldn't be used. Please use 'ynh_die' instead."
    )
if self.contains('rm -rf'):
print_error(
    "[YEP-2.12] You should avoid using 'rm -rf', please use 'ynh_secure_remove' instead"
    )
if self.contains('sed -i'):
print_warning(
    "[YEP-2.12] You should avoid using 'sed -i', please use 'ynh_replace_string' instead"
    )
if self.contains('sudo'):
print_warning(
    "[YEP-2.12] You should not need to use 'sudo', the script is being run as root. (If you need to run a command using a specific user, use 'ynh_exec_as')"
    )
if self.contains('dd if=/dev/urandom') or self.contains('openssl rand'):
print_warning(
    "Instead of 'dd if=/dev/urandom' or 'openssl rand', you might want to use ynh_string_random"
    )
if self.contains('systemctl restart nginx') or self.contains(
print_error(
    "Restarting nginx is quite dangerous (especially for web installs) and should be avoided at all cost. Use 'reload' instead."
    )
if self.name == 'install' and not self.contains('ynh_print_info'
print_warning(
    "Please add a few messages for the user, to explain what is going on (in friendly, not-too-technical terms) during the installation. You can use 'ynh_print_info' or 'ynh_script_progression' for this."
    )
