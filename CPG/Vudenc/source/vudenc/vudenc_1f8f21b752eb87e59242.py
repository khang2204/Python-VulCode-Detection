def test_run_manifest(self):...
self.mock(bot_main, 'post_error_task', lambda *args: self.fail(args))
def call_hook(botobj, name, *args):...
if name == 'on_after_task':
failure, internal_failure, dimensions, summary = args
self.mock(bot_main, 'call_hook', call_hook)
self.assertEqual(self.attributes['dimensions'], botobj.dimensions)
result = self._mock_popen(url='https://localhost:3')
self.assertEqual(False, failure)
manifest = {'command': ['echo', 'hi'], 'dimensions': {'os': 'Amiga', 'pool':
    'default'}, 'grace_period': 30, 'hard_timeout': 60, 'host':
    'https://localhost:3', 'task_id': '24'}
self.assertEqual(False, internal_failure)
self.assertEqual(self.root_dir, self.bot.base_dir)
self.assertEqual({'os': 'Amiga', 'pool': 'default'}, dimensions)
bot_main.run_manifest(self.bot, manifest, time.time())
self.assertEqual(result, summary)
