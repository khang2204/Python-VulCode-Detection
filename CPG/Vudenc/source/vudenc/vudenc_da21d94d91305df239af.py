def get(self):...
"""docstring"""
parser = reqparse.RequestParser()
parser.add_argument('building_id')
args = parser.parse_args()
where_query = 'WHERE building_id = %s' if args['building_id'] else ''
query = f'SELECT * FROM spaces {where_query}'
parameters = args['building_id'],
return database_utilities.execute_query(query, parameters)
