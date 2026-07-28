def get_visit_count():...
connection = get_connection()
cursor = connection.cursor()
cursor.execute(f'select count(*) from visitors;')
rows = cursor.fetchall()
connection.commit()
connection.close()
return rows[0][0]
