def get_remove_sort_by(self):...
new_query = []
for column in self.query_order.split('.'):
c = column.replace('-', '')
return self.get_url_with_query_params({self.ordering_query_param: '.'.join(
    new_query)})
if not int(c) == self.column_id:
new_query.append(column)
