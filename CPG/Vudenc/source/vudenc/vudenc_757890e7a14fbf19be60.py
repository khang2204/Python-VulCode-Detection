def get_user(id):...
sql_query = f"""
            SELECT * FROM {USERS_TABLE} WHERE id=%s
            """
connection = create_connection()
connection.close()
cursor = connection.cursor()
cursor.execute(sql_query, id)
user = cursor.fetchone()
if not user:
return None
return {'firstName': user['first_name'], 'lastName': user['last_name'],
    'username': user['username']}
