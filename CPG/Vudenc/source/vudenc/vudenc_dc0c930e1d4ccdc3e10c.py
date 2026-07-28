@app.route('/get_common_ingredients_with/<ingredient>')...
result = database.query_common_ingredients_with(ingredient)
if result == -1:
return None
return result
