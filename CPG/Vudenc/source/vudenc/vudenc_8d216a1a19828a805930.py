def _expected_command(self, name, store=None, verify_xss=False):...
"""docstring"""
expected_statement = (
    "DEFAULT_STORE={default_store} SCREENSHOT_DIR='{repo_dir}/test_root/log{shard_str}' BOK_CHOY_HAR_DIR='{repo_dir}/test_root/log{shard_str}/hars' BOKCHOY_A11Y_CUSTOM_RULES_FILE='{repo_dir}/{a11y_custom_file}' SELENIUM_DRIVER_LOG_DIR='{repo_dir}/test_root/log{shard_str}' VERIFY_XSS='{verify_xss}' nosetests {repo_dir}/common/test/acceptance/{exp_text} --with-xunit --xunit-file={repo_dir}/reports/bok_choy{shard_str}/xunit.xml --verbosity=2 "
    .format(default_store=store, repo_dir=REPO_DIR, shard_str='/shard_' +
    self.shard if self.shard else '', exp_text=name, a11y_custom_file=
    'node_modules/edx-custom-a11y-rules/lib/custom_a11y_rules.js',
    verify_xss=verify_xss))
return expected_statement
