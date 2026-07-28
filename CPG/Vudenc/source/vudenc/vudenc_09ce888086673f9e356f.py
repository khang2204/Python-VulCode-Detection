def edit_preset(conn, key, queryin, descriptin):...
cursor = conn.cursor()
quer = 'ALTER TABLE Presets DROP COLUMN id;'
cursor.execute(quer)
quer = (
    'ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;'
    )
cursor.execute(quer)
if queryin != 'NA':
quer = "UPDATE Presets SET querval='" + queryin + "' WHERE id=" + str(key
    ) + ';'
if descriptin != 'NA':
cursor.execute(quer)
quer = "UPDATE Presets SET description='" + descriptin + "' WHERE id=" + str(
    key) + ';'
quer = 'ALTER TABLE Presets DROP COLUMN id;'
cursor.execute(quer)
cursor.execute(quer)
quer = (
    'ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;'
    )
cursor.execute(quer)
