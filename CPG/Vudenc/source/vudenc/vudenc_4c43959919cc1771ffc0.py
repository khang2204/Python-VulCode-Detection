def _validate_option(self, default, cli):...
"""docstring"""
if not default.opt_type == bool:
if not default.opt_type == cli.opt_type:
val = cli.value.lower()
msg = 'Invalid option type for %s. Expected %s got %s'
return cli.value
if val not in ['true', 'on', 'false', 'off']:
self._exit(msg % (cli.name, default.opt_type, cli.opt_type))
msg = "Invalid value for %s. Accepted values are: 'true', 'false', 'on', 'off'"
if val in ['true', 'on']:
self._exit(msg % cli.name)
return True
return False
