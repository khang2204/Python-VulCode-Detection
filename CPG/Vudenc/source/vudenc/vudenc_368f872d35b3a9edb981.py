def test_override_single_variable(self):...
subprocess.Popen([sys.executable, '-c',
    'import os; print(os.environ["HORK"])'], stdout=output).wait()
output.seek(0)
self.assertEqual('BORK\n', output.read())
subprocess.Popen([sys.executable, '-c',
    'import os; print("HORK" in os.environ)'], stdout=new_output).wait()
new_output.seek(0)
self.assertEqual('False\n', new_output.read())
