@jwt_required...
"""docstring"""
return database_utilities.execute_query(
    f"delete from admins where email = '{email}'")
