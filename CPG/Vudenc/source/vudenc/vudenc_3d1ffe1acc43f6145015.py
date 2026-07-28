def get_all_values(self, d_name='main', t_name='inks'):...
sqlstr = 'SELECT * FROM ' + d_name + '.' + t_name + ';'
_result = self.db.execute(sqlstr).fetchall()
return _result
