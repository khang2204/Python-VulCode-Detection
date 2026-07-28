def get_preset(conn, key):...
cursor = conn.cursor()
quer = 'ALTER TABLE Presets DROP COLUMN id;'
cursor.execute(quer)
quer = (
    'ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;'
    )
cursor.execute(quer)
extable = Table('Presets')
q = MySQLQuery.from_(extable).select(extable.querval).where(extable.id == key)
print(q)
quer = str(q)
cursor.execute(quer)
row = cursor.fetchone()
strrow = str(row)
return strrow[2:-3]
