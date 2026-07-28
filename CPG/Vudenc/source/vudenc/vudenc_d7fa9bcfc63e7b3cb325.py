def san_execute(self, *cmd, **kwargs):...
if self.run_local:
return utils.execute(*cmd, **kwargs)
check_exit_code = kwargs.pop('check_exit_code', None)
command = ' '.join(cmd)
return self._run_ssh(command, check_exit_code)
