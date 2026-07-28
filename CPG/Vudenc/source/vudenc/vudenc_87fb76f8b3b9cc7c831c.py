@jwt_required...
"""docstring"""
query = f'insert into admins values (%s);'
json_data = request.get_json()
parameters = json_data['email'],
database_utilities.execute_query(query, parameters)
