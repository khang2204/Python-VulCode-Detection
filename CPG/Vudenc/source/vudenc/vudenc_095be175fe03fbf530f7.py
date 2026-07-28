def save_weeks_recipes(recipeName, row, column):...
print('save weeks')
database_file = 'meal_planner.db'
tableName = 'recipes_' + str(weekNumber)
conn.execute('CREATE TABLE IF NOT EXISTS ' + tableName +
    ' (recipe text, row int, column int)')
conn.execute('INSERT INTO ' + tableName + ' VALUES (?, ?, ?);', (recipeName,
    row, column))
