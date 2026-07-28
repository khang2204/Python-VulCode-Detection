import sqlite3
import sys
from recipe import *
def __init__(self):...
connection = sqlite3.connect('brewdie.db')
if connection:
if connection:
def store_recipe(self, recipe):...
cursor = connection.cursor()
connection.rollback()
connection.close()
connection = sqlite3.connect('brewdie.db')
print('Something went wrong')
if connection:
def load_recipes(self):...
table_names = []
sys.exit(1)
cursor = connection.cursor()
print(e)
connection.close()
recipes = []
for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'"):
recipe_names = []
if connection:
connection = sqlite3.connect('brewdie.db')
print('Something went wrong')
if connection:
return recipes
table_names.append(row[0])
if not 'Recipes' in table_names:
for row in cursor.execute('SELECT name FROM Recipes'):
connection.rollback()
return
cursor = connection.cursor()
print(e)
connection.close()
cursor.execute(
    'CREATE TABLE Recipes (name TEXT PRIMARY KEY, type TEXT, boiling_minutes INTEGER)'
    )
if not 'Malts' in table_names:
recipe_names.append(row[0])
if recipe.name in recipe_names:
for row in cursor.execute('SELECT * FROM Recipes'):
if connection:
cursor.execute(
    'CREATE TABLE Malts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, gramms REAL, recipe_name TEXT)'
    )
if not 'Rests' in table_names:
print('Recipe is already stored in the database')
cursor.execute('INSERT INTO Recipes VALUES(?, ?, ?)', (recipe.name, recipe.
    style, recipe.boiling_minutes))
recipe = Recipe(row[0], row[1], row[2])
connection.rollback()
return
cursor.execute(
    'CREATE TABLE Rests (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, degrees REAL, minutes INTEGER, position INTEGER, recipe_name TEXT)'
    )
if not 'HopDosages' in table_names:
connection.commit()
for malt_name, malt_gramms in recipe.malts.items():
for malt_row in cursor.execute("SELECT * FROM Malts WHERE recipe_name='%s'" %
cursor.execute(
    'CREATE TABLE HopDosages (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, minutes INTEGER, gramms REAL, recipe_name TEXT)'
    )
connection.commit()
cursor.execute('INSERT INTO Malts(name, gramms, recipe_name) VALUES(?, ?, ?)',
    (malt_name, malt_gramms, recipe.name))
index = 0
recipe.malts[malt_row[1]] = malt_row[2]
for rest_row in cursor.execute(
for rest in recipe.rests:
recipe.rests.append(Rest(rest_row[1], rest_row[2], rest_row[3]))
for hop_dosage_row in cursor.execute(
cursor.execute(
    'INSERT INTO Rests(name, degrees, minutes, position, recipe_name) VALUES(?, ?, ?, ?, ?)'
    , (rest.name, rest.degrees, rest.minutes, index, recipe.name))
for hop_dosage in recipe.hop_dosages:
recipe.hop_dosages.append(HopDosage(hop_dosage_row[1], hop_dosage_row[3],
    hop_dosage_row[2]))
recipes.append(recipe)
index = index + 1
cursor.execute(
    'INSERT INTO HopDosages(name, minutes, gramms, recipe_name) VALUES(?, ?, ?, ?)'
    , (hop_dosage.name, hop_dosage.minutes, hop_dosage.gramms, recipe.name))
