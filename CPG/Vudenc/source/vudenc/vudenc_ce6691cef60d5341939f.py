def prepare_connection(self, conn):...
conn.row_factory = sqlite3.Row
conn.text_factory = lambda x: str(x, 'utf-8', 'replace')
for name, num_args, func in self.sqlite_functions:
conn.create_function(name, num_args, func)
if self.sqlite_extensions:
conn.enable_load_extension(True)
if self.config('cache_size_kb'):
for extension in self.sqlite_extensions:
conn.execute('PRAGMA cache_size=-{}'.format(self.config('cache_size_kb')))
pm.hook.prepare_connection(conn=conn)
conn.execute("SELECT load_extension('{}')".format(extension))
