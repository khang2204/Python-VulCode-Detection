@app.route('/unique_ingredients/<cuisine_id>')...
logger.info('GET find_unique_ingredients_from_cuisine query')
if cuisine_id in unique_ingredients_cache:
insert_time, data = unique_ingredients_cache[cuisine_id]
cuisine_id_int = int(cuisine_id)
logger.error(
    'Error translating cuisine_id to int in find_unique_ingredients_from_cuisine, passed value: %s'
     % cuisine_id)
query_res = database.find_unique_ingredients_of_cuisine(cuisine_id_int, 500)
if datetime.now() < insert_time + cache_persistence_time:
return None
if query_res == -1:
return data
return None
if len(simplejson.loads(query_res)) == 0:
query_res = database.find_unique_ingredients_of_cuisine(cuisine_id_int, 250)
unique_ingredients_cache[cuisine_id] = datetime.now(), query_res
if query_res == -1:
return query_res
return None
unique_ingredients_cache[cuisine_id] = datetime.now(), query_res
return query_res
