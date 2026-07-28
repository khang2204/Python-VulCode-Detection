def test_run_shell_command_with_stdin(self):...
command = RunShellCommandTest.construct_testscript_command(
    'test_input_program.py')
stdout, stderr = run_shell_command(command, '1  4  10  22')
self.assertEqual(stdout, '37\n')
self.assertEqual(stderr, '')
stdout, stderr = run_shell_command(command, '1 p 5')
self.assertEqual(stdout, '')
self.assertEqual(stderr, 'INVALID INPUT\n')
