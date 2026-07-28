def add_meal(rowLocation, columnLocation):...
menu.pack_forget()
viewRecipeFrame.forget()
add_meal_frame = Frame(self, bg='#f8f8f8')
add_meal_frame.rowconfigure(0, weight=1)
add_meal_frame.columnconfigure(0, weight=1)
add_meal_frame.rowconfigure(1, weight=3)
add_meal_frame.columnconfigure(1, weight=3)
add_meal_frame.pack()
recipeNames = []
ingredientList = []
database_file = 'meal_planner.db'
cursor = conn.cursor()
selection = cursor.execute('SELECT * FROM recipe')
for result in [selection]:
for row in result.fetchall():
for i in range(len(recipeNames)):
name = row[0]
Button(add_meal_frame, text=recipeNames[i], highlightbackground='#f8f8f8',
    command=lambda x=recipeNames[i], y=ingredientList[i]: add_recipe(x, y,
    add_meal_frame, rowLocation, columnLocation)).grid(row=i, column=0)
ingredients = row[4]
recipeNames.append(name)
ingredientList.append(ingredients)
