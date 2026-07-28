def test_run_interactive_shell_command(self):...
command = RunShellCommandTest.construct_testscript_command(
    'test_interactive_program.py')
self.assertEqual(p.stdout.readline(), 'test_program X\n')
self.assertEqual(p.stdout.readline(), 'Type in a number:\n')
p.stdin.write('33\n')
p.stdin.flush()
self.assertEqual(p.stdout.readline(), '33\n')
self.assertEqual(p.stdout.readline(), 'Exiting program.\n')
