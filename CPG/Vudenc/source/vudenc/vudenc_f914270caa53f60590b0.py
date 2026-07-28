def call_hook(_botobj, name, *args):...
if name == 'on_after_task':
failure, internal_failure, dimensions, summary = args
self.assertEqual(False, failure)
self.assertEqual(True, internal_failure)
self.assertEqual({'pool': 'default'}, dimensions)
self.assertEqual({}, summary)
