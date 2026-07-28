def bugreport(self, params):...
expected = os.path.join(logging.log_path, 'AndroidDevice%s' % self.serial,
    'BugReports', 'test_something,sometime,%s' % self.serial)
assert expected in params, "Expected '%s', got '%s'." % (expected, params)
