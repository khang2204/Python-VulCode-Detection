def __init__(self2, cmd, detached, cwd, stdout, stderr, stdin, close_fds):...
self2.returncode = None
expected = [sys.executable, bot_main.THIS_FILE, 'run_isolated']
self.assertEqual(expected, cmd[:len(expected)])
self.assertEqual(True, detached)
self.assertEqual(subprocess42.PIPE, stdout)
self.assertEqual(subprocess42.STDOUT, stderr)
self.assertEqual(subprocess42.PIPE, stdin)
self.assertEqual(sys.platform != 'win32', close_fds)
