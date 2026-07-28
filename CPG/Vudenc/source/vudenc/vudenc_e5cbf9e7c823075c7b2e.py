def actually_delete(recipeName):...
queryString = '"' + recipeName + '"'
cursor = conn.cursor()
cursor.execute('DELETE FROM recipe WHERE name = ' + '"' + recipeName + '"')
print(cursor.rowcount)
if cursor.rowcount == 1:
messagebox.showinfo('Success', 'Recipe Deleted.')
if cursor.rowcount == 0:
menuFrame.pack_forget()
messagebox.showerror('Cannot Delete', 'Cannot delete recipe, please try again.'
    )
conn.close()
viewRecipeFrame.pack(expand=True, fill='both')
