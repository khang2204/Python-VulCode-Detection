@app.route('/get_cuisines')...
query_res = database.get_cuisines()
if query_res == -1:
return None
logger.info('GET get_cuisines query')
return query_res
