def _get_base_query(self, query=None, filters=None, order_column='',...
if filters:
query = filters.apply_all(query)
if order_column != '':
if hasattr(self.obj, order_column):
return query
if hasattr(getattr(self.obj, order_column), '_col_name'):
query = query.order_by(order_column + ' ' + order_direction)
order_column = getattr(getattr(self.obj, order_column), '_col_name')
