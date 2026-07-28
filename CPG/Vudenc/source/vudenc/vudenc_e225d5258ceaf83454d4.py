def print_states_N(db):...
"""docstring"""
cur = db.cursor()
cur.execute(
    "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
rows = cur.fetchall()
for row in rows:
print(row)
cur.close()
db.close()
