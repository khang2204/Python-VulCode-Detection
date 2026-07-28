@jwt_required...
"""docstring"""
query = f'insert into spaces values (%s, %s, %s, %s, %s);'
json_data = request.get_json()
parameters = json_data['space_id'], json_data['building_id'], json_data['name'
    ], json_data['capacity'], json_data['features']
database_utilities.execute_query(query, parameters)
