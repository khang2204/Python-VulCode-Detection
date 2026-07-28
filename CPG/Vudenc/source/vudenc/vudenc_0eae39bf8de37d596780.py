def test_generate_html_reports(self):...
suite = Pa11yCrawler('')
suite.generate_html_reports()
self._mock_sh.assert_has_calls([call(
    'pa11ycrawler json-to-html --pa11ycrawler-reports-dir={}'.format(suite.
    pa11y_report_dir))])
