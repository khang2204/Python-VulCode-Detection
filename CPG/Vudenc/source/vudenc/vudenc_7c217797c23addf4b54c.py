def query_simple_group(self, group_by='', aggregate_func=None,...
query = self.session.query(self.obj)
query = self._get_base_query(query=query, filters=filters)
query_result = query.all()
group = GroupByCol(group_by, 'Group by')
return group.apply(query_result)
