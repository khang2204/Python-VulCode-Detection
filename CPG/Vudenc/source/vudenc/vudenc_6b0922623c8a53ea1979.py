def get_connection_tuple(connection_string):...
"""docstring"""
connection_array = connection_string.split('@')
if len(connection_array) == 2:
username = connection_array[0]
return None, None
servername = connection_array[1]
return username, servername
