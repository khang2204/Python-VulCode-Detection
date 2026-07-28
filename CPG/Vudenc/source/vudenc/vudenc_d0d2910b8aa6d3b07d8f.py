def view_recipes():...
frame.pack_forget()
viewRecipeFrame.pack(expand=True, fill='both')
database_file = 'meal_planner.db'
cursor = conn.cursor()
selection = cursor.execute('SELECT * FROM recipe')
for result in [selection]:
for row in result.fetchall():
conn.close()
name = row[0]
for i in range(len(recipeNames)):
recipeNames.append(name)
label = Label(viewRecipeFrame, font=MEDIUM_FONT, bg='#f8f8f8', fg='#000000',
    text=recipeNames[i])
label.pack()
label.bind('<Button-1>', lambda event, x=recipeNames[i]: [callback(x),
    viewRecipeFrame.pack_forget()])
