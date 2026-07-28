def test_run_shell_command_without_stdin(self):...
command = RunShellCommandTest.construct_testscript_command('test_program.py')
stdout, stderr = run_shell_command(command)
expected = """test_program Z
non-interactive mode.
Exiting...
"""
self.assertEqual(stdout, expected)
self.assertEqual(stderr, '')
