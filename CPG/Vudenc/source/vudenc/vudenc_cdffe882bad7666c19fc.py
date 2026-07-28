def update_users(repository):...
"""docstring"""
if os.environ.get('OVER_HEROKU', False) is not False:
query = ("INSERT INTO Users (repository, created_at) VALUES ('{}', now());"
    .format(repository))
cursor.execute(query)
conn.rollback()
conn.commit()
