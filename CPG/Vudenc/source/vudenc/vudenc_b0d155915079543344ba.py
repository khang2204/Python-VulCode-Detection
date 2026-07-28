def execute_query(self, connection_url, query):...
engine = self._get_engine(connection_url)
result = self._execute_with_engine(engine, query)
return QueryResult.from_sqlalchemy_result(result)
