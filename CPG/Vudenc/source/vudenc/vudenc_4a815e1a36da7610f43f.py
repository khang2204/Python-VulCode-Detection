import sys
import os.path
import argparse
import sqlite3
import codecs
"""Database abstraction class for Ecological Shopping List II.
       All database related functions are implemented as an API.
    """
def __init__(self, db_path):...
"""docstring"""
self.connection = False
self.db_path = db_path
if os.path.exists(self.db_path) and os.path.isfile(self.db_path):
self.connection = sqlite3.connect(self.db_path)
print('db does not exist')
self.cursor = self.connection.cursor()
def create_empty_database(self):...
"""docstring"""
if self.connection:
print('Database already open! Please choose another file name.')
sql = (
    'BEGIN TRANSACTION;                 CREATE TABLE item (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, shoppinglistid INTEGER);                 CREATE UNIQUE INDEX itidname ON item (id, shoppinglistid);                 CREATE TABLE itemlanguage (id INTEGER PRIMARY KEY AUTOINCREMENT, language TEXT);                 CREATE UNIQUE INDEX idlanguage ON itemlanguage (id, language ASC);                 CREATE TABLE itemtranslation (id INTEGER PRIMARY KEY AUTOINCREMENT, itemid INTEGER, itemlanguageid INTEGER, translation TEXT);                 CREATE UNIQUE INDEX iditemlanguageid ON itemtranslation (id, itemlanguageid ASC);                 CREATE TABLE shoppinglist (id INTEGER PRIMARY KEY AUTOINCREMENT, hash TEXT);                 CREATE UNIQUE INDEX idhash ON shoppinglist (id, hash ASC);                 CREATE TABLE shoppinglistitems (id INTEGER PRIMARY KEY AUTOINCREMENT, shoppinglistid INTEGER, itemid INTEGER, amount INTEGER);                 CREATE UNIQUE INDEX idshoppinglistid ON shoppinglistitems (id, shoppinglistid ASC);                 CREATE TABLE store (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);                 CREATE UNIQUE INDEX stidname ON store (id, name ASC);                 CREATE TABLE price (id INTEGER PRIMARY KEY AUTOINCREMENT, itemid INTEGER, storeid INTEGER, price REAL);                 CREATE UNIQUE INDEX pridstoreid ON price (id, storeid ASC);                 CREATE TABLE shoppingorder (id INTEGER PRIMARY KEY AUTOINCREMENT, storeid INTEGER, itemid INTEGER, shorder INTEGER);                 CREATE UNIQUE INDEX soidstoreid ON shoppingorder (id, storeid ASC);                 COMMIT;'
    )
def import_database(self, sqlfile):...
self.connection = sqlite3.connect(self.db_path)
"""docstring"""
self.cursor = self.connection.cursor()
self.connection = sqlite3.connect(self.db_path)
self.cursor.executescript(sql)
self.cursor = self.connection.cursor()
if self.connection:
f = codecs.open(sqlfile[0], encoding='utf-8', mode='r')
def dump_database(self, sqlfile):...
sql = f.read()
"""docstring"""
self.cursor.executescript(sql)
if self.connection:
print('db created and contents imported from %s' % sqlfile[0])
for line in self.connection.iterdump():
def find_all_items(self, langid):...
f.write('%s\n' % line)
print('db dumped to %s' % sqlfile[0])
"""docstring"""
if langid[0] == '0':
return self.cursor.execute('select * from item')
return self.cursor.execute(
    'select item.id, item.shoppinglistid, item.name,                 itemtranslation.id, itemtranslation.itemid, itemtranslation.itemlanguageid,                 itemtranslation.translation                 from item                 left join itemtranslation                 on itemtranslation.itemlanguageid = "%s" and itemtranslation.itemid = item.id'
     % langid[0])
