def list(self, where=None):...
"""docstring"""
model_cls = self.resource_type
query = self.session.query(model_cls, count().over())
limit = self._query_arg('limit', int)
offset = self._query_arg('offset', int)
deleted = self._query_arg('show_deleted', bool, False)
search_term = self._query_arg('search')
regex = self._query_arg('regex', bool, False)
search_fields = self._query_arg('search_fields', list, default=['title'])
search_lang = self._query_arg('lang')
default_sort = ['{}:DESC'.format(self.default_sort_column_name)]
order_by_text = (element.split(':') for element in self._query_arg(
    'order_by', list, default=default_sort))
type_constraint = self._query_arg('type')
if search_term is not None:
for search_field in search_fields:
if not deleted:
query = column_search(query, model_cls=model_cls, column_name=search_field,
    search_term=search_term, language=search_lang, regex=regex)
query = query.filter(model_cls.deleted == false())
if type_constraint is not None:
query = query.filter(model_cls.type_constraint == type_constraint)
if where is not None:
query = query.filter(where)
for attribute_name, direction in order_by_text:
if limit is not None:
order = getattr(model_cls, attribute_name)
order = text('{} {} NULLS LAST'.format(attribute_name, direction))
query = query.order_by(order)
query = query.limit(limit)
if offset is not None:
direction = direction.lower()
query = query.offset(offset)
result = query.all()
if direction == 'asc':
if result:
order = order.asc()
if direction == 'desc':
num_filtered = result[0][1]
return 0, []
order = order.nullslast()
order = order.desc()
models = [res[0] for res in result]
return num_filtered, self._specific_fields(models, is_detail=False)
