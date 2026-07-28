def print_library_info(cnxn):...
import pyodbc
print('python:  %s' % sys.version)
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
row = cursor.fetchone()
print('Max %s = %s' % (typename, row and row[2] or '(not supported)'))
