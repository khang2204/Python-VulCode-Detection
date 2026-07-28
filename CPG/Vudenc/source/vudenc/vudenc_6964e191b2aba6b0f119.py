def create_table(self):...
stmt = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(tb_name, mapping)
self.connection.execute(stmt)
self.connection.commit()
