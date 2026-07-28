@jwt_required...
"""docstring"""
return database_utilities.execute_query(
    f'delete from spaces where space_id = %s', (space_id,))
