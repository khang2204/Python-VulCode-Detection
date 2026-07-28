def load_recipes(self):...
recipes = []
connection = sqlite3.connect('brewdie.db')
print('Something went wrong')
if connection:
return recipes
cursor = connection.cursor()
print(e)
connection.close()
for row in cursor.execute('SELECT * FROM Recipes'):
if connection:
recipe = Recipe(row[0], row[1], row[2])
connection.rollback()
return
for malt_row in cursor.execute("SELECT * FROM Malts WHERE recipe_name='%s'" %
recipe.malts[malt_row[1]] = malt_row[2]
for rest_row in cursor.execute(
recipe.rests.append(Rest(rest_row[1], rest_row[2], rest_row[3]))
for hop_dosage_row in cursor.execute(
recipe.hop_dosages.append(HopDosage(hop_dosage_row[1], hop_dosage_row[3],
    hop_dosage_row[2]))
recipes.append(recipe)
