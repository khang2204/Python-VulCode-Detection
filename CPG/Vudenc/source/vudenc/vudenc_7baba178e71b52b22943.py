@jwt_required...
"""docstring"""
query = f'update users set user_id = %s '
query += f"where user_id = '{user_id}'"
json_data = request.get_json()
parameters = json_data['user_id'],
database_utilities.execute_query(query, parameters)
