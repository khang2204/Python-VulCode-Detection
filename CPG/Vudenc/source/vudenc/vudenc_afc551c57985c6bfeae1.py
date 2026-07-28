def run_extra_cmd(self):...
if not self.get_option('no-database') and self.conf:
return self.collect_database()
return False
