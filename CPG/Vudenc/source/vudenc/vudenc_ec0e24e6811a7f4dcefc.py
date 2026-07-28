def test_default(self):...
suite = Pa11yCrawler('')
self.assertEqual(suite.cmd, self._expected_command(suite.pa11y_report_dir,
    suite.start_urls))
