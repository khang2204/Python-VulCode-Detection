import pyxl
import mysql.connector
from pypika import MySQLQuery, Table, Field
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
def remove_preset(conn, key):...
cursor = conn.cursor()
quer = 'ALTER TABLE Presets DROP COLUMN id;'
cursor.execute(quer)
quer = (
    'ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;'
    )
cursor.execute(quer)
quer = 'DELETE FROM Presets WHERE id = ' + key
cursor.execute(quer)
quer = 'ALTER TABLE Presets DROP COLUMN id;'
cursor.execute(quer)
quer = (
    'ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;'
    )
cursor.execute(quer)
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
