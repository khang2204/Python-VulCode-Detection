def query_month_group(self, group_by='', filters=None):...
query = self.session.query(self.obj)
query = self._get_base_query(query=query, filters=filters)
query_result = query.all()
group = GroupByDateMonth(group_by, 'Group by Month')
return group.apply(query_result)
