def lint(self, filename=None, file=None):...
"""docstring"""
assert self.use_stdin and file is not None or not self.use_stdin and filename is not None
config_file = self.generate_config_file()
self.command = self._create_command(filename=filename, config_file=config_file)
stdin_input = ''.join(file) if self.use_stdin else None
stdout_output, stderr_output = run_shell_command(self.command, stdin=
    stdin_input)
self.stdout_output = tuple(stdout_output.splitlines(keepends=True))
self.stderr_output = tuple(stderr_output.splitlines(keepends=True))
results_output = self.stderr_output if self.use_stderr else self.stdout_output
results = self.process_output(results_output, filename, file)
if not self.use_stderr:
self._print_errors(self.stderr_output)
if config_file:
os.remove(config_file)
return results
