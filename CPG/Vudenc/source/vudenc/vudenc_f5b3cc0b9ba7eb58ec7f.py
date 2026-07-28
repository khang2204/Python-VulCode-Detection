def _mock_popen(self, returncode=0, exit_code=0, url='https://localhost:1'):...
result = {'exit_code': exit_code, 'must_signal_internal_failure': None,
    'version': 3}
def __init__(self2, cmd, detached, cwd, env, stdout, stderr, stdin, close_fds):...
self2.returncode = None
self2._out_file = os.path.join(self.root_dir, 'work', 'task_runner_out.json')
expected = [sys.executable, bot_main.THIS_FILE, 'task_runner',
    '--swarming-server', url, '--in-file', os.path.join(self.root_dir,
    'work', 'task_runner_in.json'), '--out-file', self2._out_file,
    '--cost-usd-hour', '3600.0', '--start', '100.0', '--min-free-space',
    str(int((os_utilities.get_min_free_space(bot_main.THIS_FILE) + 250.0) *
    1024 * 1024))]
self.assertEqual(expected, cmd)
self.assertEqual(True, detached)
self.assertEqual(self.bot.base_dir, cwd)
self.assertEqual('24', env['SWARMING_TASK_ID'])
self.assertTrue(stdout)
self.assertEqual(subprocess42.STDOUT, stderr)
self.assertEqual(subprocess42.PIPE, stdin)
self.assertEqual(sys.platform != 'win32', close_fds)
def wait(self2, timeout=None):...
self2.returncode = returncode
json.dump(result, f)
return 0
