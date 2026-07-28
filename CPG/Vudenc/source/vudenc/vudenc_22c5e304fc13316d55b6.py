def _expected_command(self, report_dir, start_urls):...
"""docstring"""
expected_statement = (
    'pa11ycrawler run {start_urls} --pa11ycrawler-allowed-domains=localhost --pa11ycrawler-reports-dir={report_dir} --pa11ycrawler-deny-url-matcher=logout --pa11y-reporter="1.0-json" --depth-limit=6 '
    .format(start_urls=' '.join(start_urls), report_dir=report_dir))
return expected_statement
