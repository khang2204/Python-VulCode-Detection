import os
import six
import testtools
from bandit.core import config as b_config
from bandit.core import constants as C
from bandit.core import manager as b_manager
from bandit.core import metrics
from bandit.core import test_set as b_test_set
"""Functional tests for bandit test plugins.

    This set of tests runs bandit against each example file in turn
    and records the score returned. This is compared to a known good value.
    When new tests are added to an example the expected result should be
    adjusted to match.
    """
def setUp(self):...
super(FunctionalTests, self).setUp()
path = os.path.join(os.getcwd(), 'bandit', 'plugins')
b_conf = b_config.BanditConfig()
self.b_mgr = b_manager.BanditManager(b_conf, 'file')
self.b_mgr.b_conf._settings['plugins_dir'] = path
self.b_mgr.b_ts = b_test_set.BanditTestSet(config=b_conf)
def run_example(self, example_script, ignore_nosec=False):...
"""docstring"""
path = os.path.join(os.getcwd(), 'examples', example_script)
self.b_mgr.ignore_nosec = ignore_nosec
self.b_mgr.discover_files([path], True)
self.b_mgr.run_tests()
def check_example(self, example_script, expect, ignore_nosec=False):...
"""docstring"""
self.b_mgr.scores = []
self.run_example(example_script, ignore_nosec=ignore_nosec)
expected = 0
result = 0
for test_scores in self.b_mgr.scores:
for score_type in test_scores:
self.assertEqual(expected, result)
self.assertIn(score_type, expect)
def check_metrics(self, example_script, expect):...
for rating in expect[score_type]:
"""docstring"""
expected += expect[score_type][rating] * C.RANKING_VALUES[rating]
result += sum(test_scores[score_type])
self.b_mgr.metrics = metrics.Metrics()
self.b_mgr.scores = []
self.run_example(example_script)
m = self.b_mgr.metrics.data
for k in expect:
if k != 'issues':
if 'issues' in expect:
self.assertEqual(expect[k], m['_totals'][k])
for criteria, default in C.CRITERIA:
def test_binding(self):...
for rank in C.RANKING:
"""docstring"""
label = '{0}.{1}'.format(criteria, rank)
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'MEDIUM': 1}}
expected = 0
self.check_example('binding.py', expect)
if expect['issues'].get(criteria, None).get(rank, None):
def test_crypto_md5(self):...
expected = expect['issues'][criteria][rank]
self.assertEqual(expected, m['_totals'][label])
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 11}, 'CONFIDENCE': {'HIGH': 11}}
self.check_example('crypto-md5.py', expect)
def test_ciphers(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 13}, 'CONFIDENCE': {'HIGH': 13}}
self.check_example('ciphers.py', expect)
def test_cipher_modes(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('cipher-modes.py', expect)
def test_eval(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('eval.py', expect)
def test_mark_safe(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('mark_safe.py', expect)
def test_exec(self):...
"""docstring"""
filename = 'exec-{}.py'
if six.PY2:
filename = filename.format('py2')
filename = filename.format('py3')
expect = {'SEVERITY': {'MEDIUM': 2}, 'CONFIDENCE': {'HIGH': 2}}
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example(filename, expect)
def test_exec_as_root(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 5}, 'CONFIDENCE': {'MEDIUM': 5}}
self.check_example('exec-as-root.py', expect)
def test_hardcoded_passwords(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 7}, 'CONFIDENCE': {'MEDIUM': 7}}
self.check_example('hardcoded-passwords.py', expect)
def test_hardcoded_tmp(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'MEDIUM': 3}}
self.check_example('hardcoded-tmp.py', expect)
def test_httplib_https(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('httplib_https.py', expect)
def test_imports_aliases(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 4, 'MEDIUM': 5, 'HIGH': 0}, 'CONFIDENCE': {
    'HIGH': 9}}
self.check_example('imports-aliases.py', expect)
def test_imports_from(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('imports-from.py', expect)
def test_imports_function(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('imports-function.py', expect)
def test_telnet_usage(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('telnetlib.py', expect)
def test_ftp_usage(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('ftplib.py', expect)
def test_imports(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('imports.py', expect)
def test_mktemp(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 4}, 'CONFIDENCE': {'HIGH': 4}}
self.check_example('mktemp.py', expect)
def test_nonsense(self):...
"""docstring"""
self.run_example('nonsense.py')
self.assertEqual(1, len(self.b_mgr.skipped))
def test_okay(self):...
"""docstring"""
expect = {'SEVERITY': {}, 'CONFIDENCE': {}}
self.check_example('okay.py', expect)
def test_os_chmod(self):...
"""docstring"""
filename = 'os-chmod-{}.py'
if six.PY2:
filename = filename.format('py2')
filename = filename.format('py3')
expect = {'SEVERITY': {'MEDIUM': 2, 'HIGH': 8}, 'CONFIDENCE': {'MEDIUM': 1,
    'HIGH': 9}}
self.check_example(filename, expect)
def test_os_exec(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 8}, 'CONFIDENCE': {'MEDIUM': 8}}
self.check_example('os-exec.py', expect)
def test_os_popen(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 8, 'MEDIUM': 0, 'HIGH': 1}, 'CONFIDENCE': {
    'HIGH': 9}}
self.check_example('os-popen.py', expect)
def test_os_spawn(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 8}, 'CONFIDENCE': {'MEDIUM': 8}}
self.check_example('os-spawn.py', expect)
def test_os_startfile(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 3}, 'CONFIDENCE': {'MEDIUM': 3}}
self.check_example('os-startfile.py', expect)
def test_os_system(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('os_system.py', expect)
def test_pickle(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 2, 'MEDIUM': 6}, 'CONFIDENCE': {'HIGH': 8}}
self.check_example('pickle_deserialize.py', expect)
def test_popen_wrappers(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 7}, 'CONFIDENCE': {'HIGH': 7}}
self.check_example('popen_wrappers.py', expect)
def test_random_module(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 6}, 'CONFIDENCE': {'HIGH': 6}}
self.check_example('random_module.py', expect)
def test_requests_ssl_verify_disabled(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 7}, 'CONFIDENCE': {'HIGH': 7}}
self.check_example('requests-ssl-verify-disabled.py', expect)
def test_skip(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 5}, 'CONFIDENCE': {'HIGH': 5}}
self.check_example('skip.py', expect)
def test_ignore_skip(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 7}, 'CONFIDENCE': {'HIGH': 7}}
self.check_example('skip.py', expect, ignore_nosec=True)
def test_sql_statements(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 12}, 'CONFIDENCE': {'LOW': 7, 'MEDIUM': 5}}
self.check_example('sql_statements.py', expect)
def test_ssl_insecure_version(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1, 'MEDIUM': 10, 'HIGH': 7}, 'CONFIDENCE': {
    'LOW': 0, 'MEDIUM': 11, 'HIGH': 7}}
self.check_example('ssl-insecure-version.py', expect)
def test_subprocess_shell(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 3, 'MEDIUM': 1, 'LOW': 14}, 'CONFIDENCE': {
    'HIGH': 17, 'LOW': 1}}
self.check_example('subprocess_shell.py', expect)
def test_urlopen(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 14}, 'CONFIDENCE': {'HIGH': 14}}
self.check_example('urlopen.py', expect)
def test_utils_shell(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 5}, 'CONFIDENCE': {'HIGH': 5}}
self.check_example('utils-shell.py', expect)
def test_wildcard_injection(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 4, 'MEDIUM': 0, 'LOW': 10}, 'CONFIDENCE': {
    'MEDIUM': 5, 'HIGH': 9}}
self.check_example('wildcard-injection.py', expect)
def test_yaml(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('yaml_load.py', expect)
def test_jinja2_templating(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 4}, 'CONFIDENCE': {'HIGH': 3, 'MEDIUM': 1}}
self.check_example('jinja2_templating.py', expect)
def test_secret_config_option(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1, 'MEDIUM': 2}, 'CONFIDENCE': {'MEDIUM': 3}}
self.check_example('secret-config-option.py', expect)
def test_mako_templating(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('mako_templating.py', expect)
def test_xml(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 4}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 4}}
self.check_example('xml_etree_celementtree.py', expect)
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 2}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 2}}
self.check_example('xml_expatbuilder.py', expect)
expect = {'SEVERITY': {'LOW': 3, 'HIGH': 1}, 'CONFIDENCE': {'HIGH': 3,
    'MEDIUM': 1}}
self.check_example('xml_lxml.py', expect)
expect = {'SEVERITY': {'LOW': 2, 'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2,
    'MEDIUM': 2}}
self.check_example('xml_pulldom.py', expect)
expect = {'SEVERITY': {'HIGH': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('xml_xmlrpc.py', expect)
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 4}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 4}}
self.check_example('xml_etree_elementtree.py', expect)
expect = {'SEVERITY': {'LOW': 1, 'HIGH': 1}, 'CONFIDENCE': {'HIGH': 1,
    'MEDIUM': 1}}
self.check_example('xml_expatreader.py', expect)
expect = {'SEVERITY': {'LOW': 2, 'HIGH': 2}, 'CONFIDENCE': {'HIGH': 2,
    'MEDIUM': 2}}
self.check_example('xml_minidom.py', expect)
expect = {'SEVERITY': {'LOW': 2, 'HIGH': 6}, 'CONFIDENCE': {'HIGH': 2,
    'MEDIUM': 6}}
self.check_example('xml_sax.py', expect)
def test_httpoxy(self):...
"""docstring"""
expect = {'SEVERITY': {'HIGH': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('httpoxy_cgihandler.py', expect)
self.check_example('httpoxy_twisted_script.py', expect)
self.check_example('httpoxy_twisted_directory.py', expect)
def test_asserts(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('assert.py', expect)
def test_paramiko_injection(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 2}, 'CONFIDENCE': {'MEDIUM': 2}}
self.check_example('paramiko_injection.py', expect)
def test_partial_path(self):...
"""docstring"""
expect = {'SEVERITY': {'LOW': 11}, 'CONFIDENCE': {'HIGH': 11}}
self.check_example('partial_path_process.py', expect)
def test_try_except_continue(self):...
"""docstring"""
test = next(x for x in self.b_mgr.b_ts.tests['ExceptHandler'] if x.__name__ ==
    'try_except_continue')
test._config = {'check_typed_exception': True}
expect = {'SEVERITY': {'LOW': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('try_except_continue.py', expect)
test._config = {'check_typed_exception': False}
expect = {'SEVERITY': {'LOW': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('try_except_continue.py', expect)
def test_try_except_pass(self):...
"""docstring"""
test = next(x for x in self.b_mgr.b_ts.tests['ExceptHandler'] if x.__name__ ==
    'try_except_pass')
test._config = {'check_typed_exception': True}
expect = {'SEVERITY': {'LOW': 3}, 'CONFIDENCE': {'HIGH': 3}}
self.check_example('try_except_pass.py', expect)
test._config = {'check_typed_exception': False}
expect = {'SEVERITY': {'LOW': 2}, 'CONFIDENCE': {'HIGH': 2}}
self.check_example('try_except_pass.py', expect)
def test_metric_gathering(self):...
expect = {'nosec': 2, 'loc': 7, 'issues': {'CONFIDENCE': {'HIGH': 5},
    'SEVERITY': {'LOW': 5}}}
self.check_metrics('skip.py', expect)
expect = {'nosec': 0, 'loc': 4, 'issues': {'CONFIDENCE': {'HIGH': 2},
    'SEVERITY': {'LOW': 2}}}
self.check_metrics('imports.py', expect)
def test_weak_cryptographic_key(self):...
"""docstring"""
expect = {'SEVERITY': {'MEDIUM': 8, 'HIGH': 6}, 'CONFIDENCE': {'HIGH': 14}}
self.check_example('weak_cryptographic_key_sizes.py', expect)
def test_multiline_code(self):...
"""docstring"""
self.run_example('multiline_statement.py')
self.assertEqual(0, len(self.b_mgr.skipped))
self.assertEqual(1, len(self.b_mgr.files_list))
self.assertTrue(self.b_mgr.files_list[0].endswith('multiline_statement.py'))
issues = self.b_mgr.get_issue_list()
self.assertEqual(2, len(issues))
self.assertTrue(issues[0].fname.endswith('examples/multiline_statement.py'))
self.assertEqual(1, issues[0].lineno)
self.assertEqual(list(range(1, 3)), issues[0].linerange)
self.assertIn('subprocess', issues[0].get_code())
self.assertEqual(5, issues[1].lineno)
self.assertEqual(list(range(3, 6 + 1)), issues[1].linerange)
self.assertIn('shell=True', issues[1].get_code())
def test_code_line_numbers(self):...
self.run_example('binding.py')
issues = self.b_mgr.get_issue_list()
code_lines = issues[0].get_code().splitlines()
lineno = issues[0].lineno
self.assertEqual('%i ' % (lineno - 1), code_lines[0][:2])
self.assertEqual('%i ' % lineno, code_lines[1][:2])
self.assertEqual('%i ' % (lineno + 1), code_lines[2][:2])
def test_flask_debug_true(self):...
expect = {'SEVERITY': {'HIGH': 1}, 'CONFIDENCE': {'MEDIUM': 1}}
self.check_example('flask_debug.py', expect)
def test_nosec(self):...
expect = {'SEVERITY': {}, 'CONFIDENCE': {}}
self.check_example('nosec.py', expect)
def test_baseline_filter(self):...
issue_text = (
    'A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.'
    )
json = (
    """{
          "results": [
            {
              "code": "...",
              "filename": "%s/examples/flask_debug.py",
              "issue_confidence": "MEDIUM",
              "issue_severity": "HIGH",
              "issue_text": "%s",
              "line_number": 10,
              "line_range": [
                10
              ],
              "test_name": "flask_debug_true",
              "test_id": "B201"
            }
          ]
        }
        """
     % (os.getcwd(), issue_text))
self.b_mgr.populate_baseline(json)
self.run_example('flask_debug.py')
self.assertEqual(1, len(self.b_mgr.baseline))
self.assertEqual({}, self.b_mgr.get_issue_list())
def test_blacklist_input(self):...
expect = {'SEVERITY': {'HIGH': 1}, 'CONFIDENCE': {'HIGH': 1}}
self.check_example('input.py', expect)
