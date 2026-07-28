def create_empty_database(self):...
"""docstring"""
if self.connection:
print('Database already open! Please choose another file name.')
sql = (
    'BEGIN TRANSACTION;                 CREATE TABLE item (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, shoppinglistid INTEGER);                 CREATE UNIQUE INDEX itidname ON item (id, shoppinglistid);                 CREATE TABLE itemlanguage (id INTEGER PRIMARY KEY AUTOINCREMENT, language TEXT);                 CREATE UNIQUE INDEX idlanguage ON itemlanguage (id, language ASC);                 CREATE TABLE itemtranslation (id INTEGER PRIMARY KEY AUTOINCREMENT, itemid INTEGER, itemlanguageid INTEGER, translation TEXT);                 CREATE UNIQUE INDEX iditemlanguageid ON itemtranslation (id, itemlanguageid ASC);                 CREATE TABLE shoppinglist (id INTEGER PRIMARY KEY AUTOINCREMENT, hash TEXT);                 CREATE UNIQUE INDEX idhash ON shoppinglist (id, hash ASC);                 CREATE TABLE shoppinglistitems (id INTEGER PRIMARY KEY AUTOINCREMENT, shoppinglistid INTEGER, itemid INTEGER, amount INTEGER);                 CREATE UNIQUE INDEX idshoppinglistid ON shoppinglistitems (id, shoppinglistid ASC);                 CREATE TABLE store (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);                 CREATE UNIQUE INDEX stidname ON store (id, name ASC);                 CREATE TABLE price (id INTEGER PRIMARY KEY AUTOINCREMENT, itemid INTEGER, storeid INTEGER, price REAL);                 CREATE UNIQUE INDEX pridstoreid ON price (id, storeid ASC);                 CREATE TABLE shoppingorder (id INTEGER PRIMARY KEY AUTOINCREMENT, storeid INTEGER, itemid INTEGER, shorder INTEGER);                 CREATE UNIQUE INDEX soidstoreid ON shoppingorder (id, storeid ASC);                 COMMIT;'
    )
self.connection = sqlite3.connect(self.db_path)
self.cursor = self.connection.cursor()
self.cursor.executescript(sql)
