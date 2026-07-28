def test_run_manifest_internal_failure(self):...
posted = []
self.mock(bot_main, 'post_error_task', lambda *args: posted.append(args))
def call_hook(_botobj, name, *args):...
if name == 'on_after_task':
failure, internal_failure, dimensions, summary = args
self.mock(bot_main, 'call_hook', call_hook)
self.assertEqual(False, failure)
result = self._mock_popen(returncode=1)
self.assertEqual(True, internal_failure)
manifest = {'command': ['echo', 'hi'], 'dimensions': {'pool': 'default'},
    'grace_period': 30, 'hard_timeout': 60, 'io_timeout': 60, 'task_id': '24'}
self.assertEqual({'pool': 'default'}, dimensions)
bot_main.run_manifest(self.bot, manifest, time.time())
self.assertEqual(result, summary)
expected = [(self.bot, 'Execution failed: internal error (1).', '24')]
self.assertEqual(expected, posted)
