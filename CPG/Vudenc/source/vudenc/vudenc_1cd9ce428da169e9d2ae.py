def get_canned_query(self, database_name, query_name):...
queries = self.metadata('queries', database=database_name, fallback=False) or {
    }
query = queries.get(query_name)
if query:
if not isinstance(query, dict):
query = {'sql': query}
query['name'] = query_name
return query
