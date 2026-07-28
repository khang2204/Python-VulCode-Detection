def call_hook(_botobj, name, *args):...
if name == 'on_after_task':
failure, internal_failure, dimensions, summary = args
self.assertEqual(True, failure)
self.assertEqual(False, internal_failure)
self.assertEqual({'pool': 'default'}, dimensions)
self.assertEqual(result, summary)
