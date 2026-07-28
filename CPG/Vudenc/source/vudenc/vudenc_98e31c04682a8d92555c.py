def delete_old(self):...
last = int(time()) - one_year
stmt = 'DELETE FROM {} WHERE timestamp >= {}'.format(tb_name, str(last))
self.connection.execute(stmt)
self.connection.commit()
