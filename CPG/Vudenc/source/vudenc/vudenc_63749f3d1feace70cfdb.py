def write_preset(conn, queryin, descriptin):...
cursor = conn.cursor()
quer = 'ALTER TABLE Presets DROP COLUMN id;'
cursor.execute(quer)
quer = (
    'ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;'
    )
cursor.execute(quer)
extable = Table('Presets')
q = MySQLQuery.into(extable).columns('querval', 'description').insert(queryin,
    descriptin)
print(q)
quer = str(q)
cursor.execute(quer)
quer = 'ALTER TABLE Presets DROP COLUMN id;'
cursor.execute(quer)
quer = (
    'ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;'
    )
cursor.execute(quer)
