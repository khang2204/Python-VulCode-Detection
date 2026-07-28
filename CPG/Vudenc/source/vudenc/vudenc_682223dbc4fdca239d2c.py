def connect_sql(self, sql):...
"""docstring"""
cursor.execute(sql)
result = cursor.fetchall()
return result
