import os, sys, platform
from os.path import join, dirname, abspath, basename
import unittest
def add_to_path():...
"""docstring"""
import imp
library_exts = [t[0] for t in imp.get_suffixes() if t[-1] == imp.C_EXTENSION]
library_names = [('pyodbc%s' % ext) for ext in library_exts]
dir_suffix = '-%s.%s' % (sys.version_info[0], sys.version_info[1])
build = join(dirname(dirname(abspath(__file__))), 'build')
for root, dirs, files in os.walk(build):
for d in dirs[:]:
print(
    'Did not find the pyodbc library in the build directory.  Will use an installed version.'
    )
if not d.endswith(dir_suffix):
for name in library_names:
def print_library_info(cnxn):...
dirs.remove(d)
if name in files:
import pyodbc
sys.path.insert(0, root)
print('python:  %s' % sys.version)
return
print('pyodbc:  %s %s' % (pyodbc.version, os.path.abspath(pyodbc.__file__)))
print('odbc:    %s' % cnxn.getinfo(pyodbc.SQL_ODBC_VER))
print('driver:  %s %s' % (cnxn.getinfo(pyodbc.SQL_DRIVER_NAME), cnxn.
    getinfo(pyodbc.SQL_DRIVER_VER)))
print('         supports ODBC version %s' % cnxn.getinfo(pyodbc.
    SQL_DRIVER_ODBC_VER))
print('os:      %s' % platform.system())
print('unicode: Py_Unicode=%s SQLWCHAR=%s' % (pyodbc.UNICODE_SIZE, pyodbc.
    SQLWCHAR_SIZE))
cursor = cnxn.cursor()
for typename in ['VARCHAR', 'WVARCHAR', 'BINARY']:
t = getattr(pyodbc, 'SQL_' + typename)
if platform.system() == 'Windows':
cursor.getTypeInfo(t)
print('         %s' % ' '.join([s for s in platform.win32_ver() if s]))
def load_tests(testclass, name, *args):...
row = cursor.fetchone()
"""docstring"""
print('Max %s = %s' % (typename, row and row[2] or '(not supported)'))
if name:
if not name.startswith('test_'):
names = [method for method in dir(testclass) if method.startswith('test_')]
name = 'test_%s' % name
names = [name]
return unittest.TestSuite([testclass(name, *args) for name in names])
