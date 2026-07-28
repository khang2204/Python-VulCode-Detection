@app.route('/restaurants/<saltiness>/<sweetness>/<sourness>/<bitterness>/')...
"""docstring"""
logger.info('GET query_restaurants_by_taste query')
saltiness, sweetness, sourness, bitterness = int(saltiness), int(sweetness
    ), int(sourness), int(bitterness)
return None
restaurant_query = sql_queries.restaurant_by_taste % (get_taste_condition(
    saltiness), get_taste_condition(sweetness), get_taste_condition(
    sourness), get_taste_condition(bitterness), get_taste_condition(1 -
    saltiness), get_taste_condition(1 - sweetness), get_taste_condition(1 -
    sourness), get_taste_condition(1 - bitterness))
loclat, loclng = request.args.get('loclat'), request.args.get('loclng')
price_category = request.args.get('price_category')
online_delivery = request.args.get('online_delivery')
min_review = request.args.get('min_review')
if loclat != None and loclng != None:
lat_range = [float(loclat) - geodist, float(loclat) + geodist]
lat_range = None
lng_range = [float(loclng) - geodist, float(loclng) + geodist]
lng_range = None
filtered_query = database.restaurant_query_builder(restaurant_query,
    lat_range, lng_range, price_category, min_review, online_delivery)
limited_query = database.order_by_and_limit_query(filtered_query,
    'agg_review DESC', 20)
query_res = database.run_sql_query(limited_query)
if query_res == -1:
return None
return query_res
