def get_canned_queries(self, database_name):...
queries = self.metadata('queries', database=database_name, fallback=False) or {
    }
names = queries.keys()
return [self.get_canned_query(database_name, name) for name in names]
