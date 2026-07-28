def _cliq_run(self, verb, cliq_args, check_exit_code=True):...
"""docstring"""
cliq_arg_strings = []
for k, v in cliq_args.items():
cliq_arg_strings.append(' %s=%s' % (k, v))
cmd = verb + ''.join(cliq_arg_strings)
return self._run_ssh(cmd, check_exit_code)
