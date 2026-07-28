def test_valid_output(self):...
out = list(self.uut.process_output([
    "Random line that shouldn't be captured\n", '*************\n'],
    'a/file.py', ['original_file_lines_placeholder']))
self.assertEqual(len(out), 0)
