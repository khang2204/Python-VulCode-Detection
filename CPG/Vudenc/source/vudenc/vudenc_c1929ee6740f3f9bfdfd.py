def check_set_usage(self):...
present = False
if self.name in ['backup', 'remove']:
present = self.contains('ynh_abort_if_errors') or self.contains('set -eu')
present = self.contains('ynh_abort_if_errors')
if self.name == 'remove':
if present:
if not present:
print_error(
    '[YEP-2.4] set -eu or ynh_abort_if_errors is present. If there is a crash, it could put yunohost system in a broken state. For details, look at https://github.com/YunoHost/issues/issues/419'
    )
print_error(
    '[YEP-2.4] ynh_abort_if_errors is missing. For details, look at https://github.com/YunoHost/issues/issues/419'
    )
