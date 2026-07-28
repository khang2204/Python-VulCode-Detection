def add_recipe(recipe, ingredients, view, row, column):...
view.pack_forget()
viewRecipeFrame.forget()
searchIndex = row, column
for key, value in buttonDict.items():
if value == searchIndex:
save_weeks_recipes(recipe, row, column)
key.destroy()
save_ingredients(ingredients)
recipeLabel = Label(menu, text=recipe, bg='#f8f8f8')
recipeLabel.grid(row=row, column=column)
recipeLabel.bind('<Button-1>', lambda event: callback(recipe))
menu.pack()
