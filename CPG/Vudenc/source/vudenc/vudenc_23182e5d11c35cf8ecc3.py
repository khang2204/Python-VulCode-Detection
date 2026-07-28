from __future__ import absolute_import, division, print_function, unicode_literals
import os
import pstats
import shutil
import signal
import sys
import unittest
import uuid
import zipfile
from builtins import next, object, range, str
from contextlib import contextmanager
import mock
from future.utils import PY3
from pants.util.contextutil import InvalidZipPath, Timer, environment_as, exception_logging, hermetic_environment_as, maybe_profiled, open_zip, pushd, signal_handler_as, stdio_as, temporary_dir, temporary_file
from pants.util.process_handler import subprocess
PATCH_OPTS = dict(autospec=True, spec_set=True)
def test_empty_environment(self):...
def test_override_single_variable(self):...
subprocess.Popen([sys.executable, '-c',
    'import os; print(os.environ["HORK"])'], stdout=output).wait()
output.seek(0)
self.assertEqual('BORK\n', output.read())
subprocess.Popen([sys.executable, '-c',
    'import os; print("HORK" in os.environ)'], stdout=new_output).wait()
new_output.seek(0)
self.assertEqual('False\n', new_output.read())
def test_environment_negation(self):...
subprocess.Popen([sys.executable, '-c',
    'import os; print("HORK" in os.environ)'], stdout=output).wait()
output.seek(0)
self.assertEqual('False\n', output.read())
def test_hermetic_environment(self):...
self.assertIn('USER', os.environ)
self.assertNotIn('USER', os.environ)
def test_hermetic_environment_subprocesses(self):...
self.assertIn('USER', os.environ)
output = subprocess.check_output('env', shell=True).decode('utf-8')
self.assertNotIn('USER=', output)
self.assertIn('AAA', os.environ)
self.assertEqual(os.environ['AAA'], '333')
self.assertIn('USER', os.environ)
self.assertNotIn('AAA', os.environ)
def test_hermetic_environment_unicode(self):...
UNICODE_CHAR = '¡'
ENCODED_CHAR = UNICODE_CHAR.encode('utf-8')
expected_output = UNICODE_CHAR if PY3 else ENCODED_CHAR
self.assertEqual(os.environ['XXX'], expected_output)
self.assertIn('AAA', os.environ)
self.assertEqual(os.environ['AAA'], expected_output)
self.assertEqual(os.environ['XXX'], expected_output)
def test_simple_pushd(self):...
pre_cwd = os.getcwd()
self.assertEqual(tempdir, path)
self.assertEqual(os.path.realpath(tempdir), os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
def test_nested_pushd(self):...
pre_cwd = os.getcwd()
self.assertEqual(os.path.realpath(tempdir1), os.getcwd())
self.assertEqual(os.path.realpath(tempdir2), os.getcwd())
self.assertEqual(os.path.realpath(tempdir1), os.getcwd())
self.assertEqual(os.path.realpath(tempdir1), os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
self.assertEqual(pre_cwd, os.getcwd())
def test_temporary_file_no_args(self):...
self.assertTrue(os.path.exists(fp.name),
    'Temporary file should exist within the context.')
self.assertTrue(os.path.exists(fp.name) == False,
    'Temporary file should not exist outside of the context.')
def test_temporary_file_without_cleanup(self):...
self.assertTrue(os.path.exists(fp.name),
    'Temporary file should exist within the context.')
self.assertTrue(os.path.exists(fp.name),
    'Temporary file should exist outside of context if cleanup=False.')
os.unlink(fp.name)
def test_temporary_file_within_other_dir(self):...
self.assertTrue(os.path.realpath(f.name).startswith(os.path.realpath(path)),
    'file should be created in root_dir if specified.')
def test_temporary_dir_no_args(self):...
self.assertTrue(os.path.exists(path),
    'Temporary dir should exist within the context.')
self.assertTrue(os.path.isdir(path),
    'Temporary dir should be a dir and not a file.')
self.assertFalse(os.path.exists(path),
    'Temporary dir should not exist outside of the context.')
def test_temporary_dir_without_cleanup(self):...
self.assertTrue(os.path.exists(path),
    'Temporary dir should exist within the context.')
self.assertTrue(os.path.exists(path),
    'Temporary dir should exist outside of context if cleanup=False.')
shutil.rmtree(path)
def test_temporary_dir_with_root_dir(self):...
self.assertTrue(os.path.realpath(path2).startswith(os.path.realpath(path1)),
    'Nested temporary dir should be created within outer dir.')
def test_timer(self):...
def __init__(self):...
self._time = 0.0
def time(self):...
ret = self._time
self._time += 0.0001
return ret
