def test_hermetic_environment_subprocesses(self):...
self.assertIn('USER', os.environ)
output = subprocess.check_output('env', shell=True).decode('utf-8')
self.assertNotIn('USER=', output)
self.assertIn('AAA', os.environ)
self.assertEqual(os.environ['AAA'], '333')
self.assertIn('USER', os.environ)
self.assertNotIn('AAA', os.environ)
