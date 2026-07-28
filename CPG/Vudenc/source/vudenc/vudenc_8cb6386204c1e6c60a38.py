def run_insert(insert_stmt):...
is_success = True
conn = create_connection()
print('insert error: ', error)
return is_success
cur = conn.cursor()
is_success = False
cur.execute(insert_stmt)
results = cur.fetchall()
widths = []
columns = []
tavnit = '|'
separator = '+'
for cd in cur.description:
widths.append(max(cd[2], len(cd[0])))
for w in widths:
columns.append(cd[0])
tavnit += ' %-' + '%ss |' % (w,)
print(separator)
separator += '-' * w + '--+'
print(tavnit % tuple(columns))
print(separator)
for row in results:
print(tavnit % row)
print(separator)
conn.commit()
destroy_connection(conn)
