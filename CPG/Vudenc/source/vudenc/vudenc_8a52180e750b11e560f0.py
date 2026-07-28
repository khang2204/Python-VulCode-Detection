def is_installed(self, pkg):...
"""docstring"""
cmd = self.host.pkg_query(pkg)
res = self.run_command(cmd)
if res['status'] == 0:
return True
return False
