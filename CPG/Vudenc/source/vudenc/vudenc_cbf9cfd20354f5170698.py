def _execute_with_engine(self, engine, query):...
connection = engine.connect()
result = connection.execution_options(no_parameters=True).execute(query)
return result
