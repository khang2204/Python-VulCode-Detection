@app.route('/ingredient_prefix/<string:prefix>')...
query_res = database.find_ingredients_by_prefix(prefix)
if query_res == -1:
return None
logger.info('GET get_ingredient_by_prefix query')
return query_res
