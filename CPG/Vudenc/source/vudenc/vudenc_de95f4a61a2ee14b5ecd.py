def query(self, filters=None, order_column='', order_direction='', page=...
"""docstring"""
query = self.session.query(self.obj)
if len(order_column.split('.')) >= 2:
tmp_order_column = ''
query_count = self.session.query(func.count('*')).select_from(self.obj)
for join_relation in order_column.split('.')[:-1]:
query_count = self._get_base_query(query=query_count, filters=filters)
model_relation = self.get_related_model(join_relation)
order_column = tmp_order_column + order_column.split('.')[-1]
query = self._get_base_query(query=query, filters=filters, order_column=
    order_column, order_direction=order_direction)
query = query.join(model_relation)
count = query_count.scalar()
tmp_order_column = tmp_order_column + model_relation.__tablename__ + '.'
if page:
query = query.offset(page * page_size)
if page_size:
query = query.limit(page_size)
return count, query.all()
