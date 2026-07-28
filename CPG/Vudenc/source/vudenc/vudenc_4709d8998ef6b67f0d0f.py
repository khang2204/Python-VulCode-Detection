def run_example(self, example_script, ignore_nosec=False):...
"""docstring"""
path = os.path.join(os.getcwd(), 'examples', example_script)
self.b_mgr.ignore_nosec = ignore_nosec
self.b_mgr.discover_files([path], True)
self.b_mgr.run_tests()
