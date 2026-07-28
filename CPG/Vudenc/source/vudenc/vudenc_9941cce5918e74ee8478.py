def callback(recipeName):...
menu.pack_forget()
viewRecipeFrame.pack(expand=True, fill='both')
groceryButton.pack_forget()
database_file = 'meal_planner.db'
print(recipeName)
cursor = conn.cursor()
selection = cursor.execute('SELECT * FROM recipe WHERE name = ' + '"' +
    recipeName + '"')
for result in [selection]:
for row in result.fetchall():
Label(viewRecipeFrame, text=string, font=MEDIUM_FONT, bg='#f8f8f8', fg=
    '#000000').pack(side=TOP)
name = row[0]
Label(viewRecipeFrame, text=secondString, font=MEDIUM_FONT, bg='#f8f8f8',
    fg='#000000').pack(side=TOP)
time = row[1]
Label(viewRecipeFrame, text=thirdString, font=MEDIUM_FONT, bg='#f8f8f8', fg
    ='#000000').pack(side=TOP)
servings = row[2]
returnButton = Button(menuFrame, text='Return to Menu', highlightbackground
    ='#e7e7e7', command=lambda : [viewRecipeFrame.pack_forget(), menu.pack(
    ), returnButton.pack_forget(), label.configure(text='Meal Planer'),
    groceryButton.pack(side=RIGHT)])
ingredients = row[4]
returnButton.pack(side=RIGHT)
directions = row[5]
string = """Name: {} 
 Cook time: {} 
 Number of Servings: {} 
 """.format(name
    , time, servings)
secondString = 'Ingredients: {}'.format(ingredients)
thirdString = 'Directions: {}'.format(directions)
