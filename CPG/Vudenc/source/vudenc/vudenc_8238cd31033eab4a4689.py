@app.route('/discover_new_cuisines/<int:cuisine_id>')...
logger.info('GET discover_new_cuisines query')
if cuisine_id in cuisine_discovery_cache:
insert_time, data = cuisine_discovery_cache[cuisine_id]
query_res = database.discover_new_cuisines_from_cuisine(cuisine_id)
if datetime.now() < insert_time + cache_persistence_time:
if query_res == -1:
return data
return None
cuisine_discovery_cache[cuisine_id] = datetime.now(), query_res
return query_res
