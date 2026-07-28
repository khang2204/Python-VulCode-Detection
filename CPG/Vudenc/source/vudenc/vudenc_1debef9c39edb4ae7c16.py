def get(self, email):...
"""docstring"""
return database_utilities.execute_query(
    f"select * from admins where email = '{email}'")
