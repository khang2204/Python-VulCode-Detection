def getAlcoholByName(name):...
name = fixTypingErrors(name)
QUERY = (
    'SELECT barnivore_product_name, barnivore_status, barnivore_country ' +
    'FROM barnivore_product ' +
    "WHERE lower(barnivore_product_name) like lower('% \\%s %')")
conn = psycopg2.connect(connectionString)
print('Error %s' % e)
if conn:
return result
cur = conn.cursor()
conn.close()
cur.execute(QUERY, name)
result = cur.fetchall()
