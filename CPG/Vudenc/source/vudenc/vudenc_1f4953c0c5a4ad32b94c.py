def representation_is(self, content):...
target = cStringIO.StringIO()
self.parser.dump(target)
repr_ = target.getvalue()
target.close()
self.assertEqual(repr_, content.lstrip())
