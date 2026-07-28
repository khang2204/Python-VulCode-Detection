def insert(self, input_row):...
is_valid, violations = self.validate_row(input_row)
if is_valid:
name, location, description = input_row
return is_valid, violations
date = int(time())
args = date, name, location, description
stmt = 'INSERT INTO {} ({}) VALUES {}'.format(tb_name, columns, str(args))
self.connection.execute(stmt)
self.connection.commit()
