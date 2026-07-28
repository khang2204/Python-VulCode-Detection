def get_reverse_sort_by(self):...
new_query = []
for column in self.query_order.split('.'):
c = column.replace('-', '')
return self.get_url_with_query_params({self.ordering_query_param: '.'.join(
    new_query)})
if int(c) == self.column_id:
if column.startswith('-'):
new_query.append(column)
new_query.append(c)
new_query.append('-{}'.format(c))
