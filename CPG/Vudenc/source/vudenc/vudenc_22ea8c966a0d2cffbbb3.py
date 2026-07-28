def delete_recipe(recipeName):...
database_file = 'meal_planner.db'
now = datetime.datetime.now()
dt = datetime.date(now.year, now.month, now.day)
weekNumber = dt.isocalendar()[1]
tableName = 'recipes_' + str(weekNumber)
cursor = conn.cursor()
cursor.execute('SELECT recipe FROM ' + tableName + ' WHERE recipe = ' + '"' +
    recipeName + '"')
returnObject = cursor.fetchone()
if returnObject:
print(returnObject[0])
actually_delete(recipeName)
messagebox.showerror('Cannot Delete',
    "Cannot delete recipe when it's used in the current week's menu.")
