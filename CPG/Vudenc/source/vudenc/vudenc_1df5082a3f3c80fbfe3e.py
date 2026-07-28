import psycopg2
DBNAME = 'news'
def execute_query(cmd):...
"""docstring"""
conn = psycopg2.connect(database=DBNAME)
cursor = conn.cursor()
cursor.execute(cmd)
result = cursor.fetchall()
conn.close()
return result
