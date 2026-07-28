def test_hermetic_environment_unicode(self):...
UNICODE_CHAR = '¡'
ENCODED_CHAR = UNICODE_CHAR.encode('utf-8')
expected_output = UNICODE_CHAR if PY3 else ENCODED_CHAR
self.assertEqual(os.environ['XXX'], expected_output)
self.assertIn('AAA', os.environ)
self.assertEqual(os.environ['AAA'], expected_output)
self.assertEqual(os.environ['XXX'], expected_output)
