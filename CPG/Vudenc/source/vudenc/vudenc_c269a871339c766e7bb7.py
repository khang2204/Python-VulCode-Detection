usage = """usage: %prog [options] connection_string

Unit tests for SQLite using the ODBC driver from http://www.ch-werner.de/sqliteodbc

To use, pass a connection string as the parameter. The tests will create and
drop tables t1 and t2 as necessary.  On Windows, use the 32-bit driver with
32-bit Python and the 64-bit driver with 64-bit Python (regardless of your
operating system bitness).

These run using the version from the 'build' directory, not the version
installed into the Python directories.  You must run python setup.py build
before running the tests.

You can also put the connection string into a setup.cfg file in the root of the project
(the same one setup.py would use) like so:

  [sqlitetests]
  connection-string=Driver=SQLite3 ODBC Driver;Database=sqlite.db
"""
import sys, os, re
import unittest
from decimal import Decimal
from datetime import datetime, date, time
from os.path import join, getsize, dirname, abspath
from testutils import *
_TESTSTR = '0123456789-abcdefghijklmnopqrstuvwxyz-'
def _generate_test_string(length):...
"""docstring"""
if length <= len(_TESTSTR):
return _TESTSTR[:length]
c = (length + len(_TESTSTR) - 1) // len(_TESTSTR)
v = _TESTSTR * c
return v[:length]
