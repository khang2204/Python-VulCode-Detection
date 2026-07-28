def callback(recipeName):...
viewRecipeFrame.pack_forget()
database_file = 'meal_planner.db'
menuFrame.pack(fill='both')
load = Image.open('home.jpg')
render = ImageTk.PhotoImage(load)
img = Button(menuFrame, image=render, borderwidth=0, highlightthickness=0,
    highlightbackground='#e7e7e7', command=lambda : [frame.pack(expand=True,
    fill='both'), menuFrame.pack_forget(), viewDetailsFrame.pack_forget()])
img.image = render
img.pack(side=LEFT)
label = Label(menuFrame, text='View Recipe', font=LARGE_FONT, bg='#e7e7e7',
    fg='#272822')
label.pack(side=LEFT, padx=300)
viewDetailsFrame = Frame(self, bg='#f8f8f8')
viewDetailsFrame.pack(expand=True, fill='both')
cursor = conn.cursor()
selection = cursor.execute('SELECT * FROM recipe WHERE name = ' + '"' +
    recipeName + '"')
for result in [selection]:
for row in result.fetchall():
string = (
    """Name: {} 
 Cook time: {} 
 Number of Servings: {} 
 Ingredients: {} 
 Directions: {}"""
    .format(name, time, servings, ingredients, directions))
name = row[0]
Label(viewDetailsFrame, text=string, font=MEDIUM_FONT, bg='#f8f8f8', fg=
    '#000000').pack(side=LEFT)
time = row[1]
conn.close()
servings = row[2]
Button(menuFrame, text='Delete', highlightbackground='#e7e7e7', command=lambda
    : delete_recipe(name)).pack(side=RIGHT)
favorite = row[3]
ingredients = row[4]
directions = row[5]
