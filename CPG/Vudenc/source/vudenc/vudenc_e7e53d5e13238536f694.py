def get_add_sort_by(self):...
if not self.is_ordered():
if self.query_order:
if self.current_columns_length > 1:
return self.get_url_with_query_params({self.ordering_query_param: '{}.{}'.
    format(self.column_id, self.query_order)})
return self.get_url_with_query_params({self.ordering_query_param: self.
    column_id})
new_query = []
return self.get_reverse_sort_by()
for column in self.query_order.split('.'):
c = column.replace('-', '')
if not self.is_reverse() and self.current_columns[0] == self.column_id:
if not int(c) == self.column_id:
return self.get_url_with_query_params({self.ordering_query_param: '-{}.{}'.
    format(self.column_id, '.'.join(new_query))})
return self.get_url_with_query_params({self.ordering_query_param: '{}.{}'.
    format(self.column_id, '.'.join(new_query))})
new_query.append(column)
