def get_subjects():...
cur = conn.cursor()
query = 'SELECT subject, count(*) FROM articles group by subject;'
cur.execute(query)
subjects = sorted(cur.fetchall(), key=lambda tup: tup[0])
return subjects
