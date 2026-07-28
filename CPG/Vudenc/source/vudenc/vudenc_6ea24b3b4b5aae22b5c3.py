def get(self, space_id):...
"""docstring"""
return database_utilities.execute_query(
    f"select * from spaces where space_id = '{space_id}'")
