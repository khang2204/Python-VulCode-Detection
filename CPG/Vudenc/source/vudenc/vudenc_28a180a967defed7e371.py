@jwt_required...
"""docstring"""
query = f'insert into users values (%s);'
json_data = request.get_json()
parameters = json_data['user_id'],
database_utilities.execute_query(query, parameters)
