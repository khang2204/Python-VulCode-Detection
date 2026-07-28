def query_year_group(self, group_by='', filters=None):...
query = self.session.query(self.obj)
query = self._get_base_query(query=query, filters=filters)
query_result = query.all()
group_year = GroupByDateYear(group_by, 'Group by Year')
return group_year.apply(query_result)
