def call_hook(botobj, name, *args):...
if name == 'on_after_task':
failure, internal_failure, dimensions, summary = args
self.assertEqual(self.attributes['dimensions'], botobj.dimensions)
self.assertEqual(False, failure)
self.assertEqual(False, internal_failure)
self.assertEqual({'os': 'Amiga', 'pool': 'default'}, dimensions)
self.assertEqual(result, summary)
