def test_gives_corrected(self):...
self.uut.gives_corrected = True
out = tuple(self.uut.process_output(['a', 'b'], 'filename', ['a', 'b']))
self.assertEqual((), out)
out = tuple(self.uut.process_output(['a', 'b'], 'filename', ['a']))
self.assertEqual(len(out), 1)
