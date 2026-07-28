def is_reverse(self):...
for column in self.query_order.split('.'):
c = column.replace('-', '')
return False
if int(c) == self.column_id:
if column.startswith('-'):
return True
