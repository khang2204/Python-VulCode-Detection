def get(self, user_id):...
"""docstring"""
return database_utilities.execute_query(
    f"select * from users where user_id = '{user_id}'")
