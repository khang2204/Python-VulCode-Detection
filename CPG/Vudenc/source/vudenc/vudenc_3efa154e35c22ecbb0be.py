@jwt_required...
"""docstring"""
return database_utilities.execute_query(
    f"delete from users where user_id = '{user_id}'")
