def test_environment_negation(self):...
subprocess.Popen([sys.executable, '-c',
    'import os; print("HORK" in os.environ)'], stdout=output).wait()
output.seek(0)
self.assertEqual('False\n', output.read())
