@jwt_required...
"""docstring"""
query = f'update spaces set space_id = %s, building_id = %s, '
query += f'name = %s, capacity = %s, features = %s '
query += f"where space_id = '{space_id}'"
json_data = request.get_json()
parameters = json_data['space_id'], json_data['building_id'], json_data['name'
    ], json_data['capacity'], json_data['features']
database_utilities.execute_query(query, parameters)
