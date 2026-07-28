def save_ingredients(ingredients):...
database_file = 'meal_planner.db'
tableName = 'ingredients_' + str(weekNumber)
conn.execute('CREATE TABLE IF NOT EXISTS ' + tableName + ' (ingredients text)')
conn.execute('INSERT INTO ' + tableName + ' VALUES (?);', (ingredients,))
