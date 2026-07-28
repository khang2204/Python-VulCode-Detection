def test_run_manifest_exception(self):...
posted = []
def post_error_task(botobj, msg, task_id):...
posted.append((botobj, msg.splitlines()[0], task_id))
self.mock(bot_main, 'post_error_task', post_error_task)
def call_hook(_botobj, name, *args):...
if name == 'on_after_task':
failure, internal_failure, dimensions, summary = args
self.mock(bot_main, 'call_hook', call_hook)
self.assertEqual(False, failure)
def raiseOSError(*_a, **_k):...
self.assertEqual(True, internal_failure)
self.mock(subprocess42, 'Popen', raiseOSError)
self.assertEqual({'pool': 'default'}, dimensions)
manifest = {'command': ['echo', 'hi'], 'dimensions': {'pool': 'default'},
    'grace_period': 30, 'hard_timeout': 60, 'task_id': '24'}
self.assertEqual({}, summary)
bot_main.run_manifest(self.bot, manifest, time.time())
expected = [(self.bot, 'Internal exception occured: Dang', '24')]
self.assertEqual(expected, posted)
