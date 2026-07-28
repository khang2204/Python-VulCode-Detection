def setup(self):...
self.pg_pass = False
if not self.get_option('no-database'):
self.conf = self.parse_db_conf()
self.format_db_cmd()
