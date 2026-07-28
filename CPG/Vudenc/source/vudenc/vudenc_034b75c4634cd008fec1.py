def check_for_setup_error(self):...
"""docstring"""
if not self.run_local:
if not (self.configuration.san_password or self.configuration.san_private_key):
if not self.configuration.san_ip:
