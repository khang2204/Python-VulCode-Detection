def get(self, request):...
item = request.query_params.get('item')
city = request.query_params.get('city')
if not item and not city:
return Response(NOT_FOUND_JSON_RESPONSE)
sql = """SELECT
                    mode() WITHIN GROUP (ORDER BY list_price DESC) AS model_value,
                    count(*)
                 FROM
                    "itemPrices_itemsale"
              """
if item and city:
sql = "{} WHERE city = '{}' and title = '{}'".format(sql, city, item)
if item:
c.execute(sql)
sql = "{} WHERE title = '{}'".format(sql, item)
if city:
price_mode, count = c.fetchone()
sql = "{} WHERE city = '{}'".format(sql, city)
if count == 0:
return Response(NOT_FOUND_JSON_RESPONSE)
return Response({'status': 200, 'content': {'item': item or 'Not specified',
    'item_count': count, 'price_suggestion': price_mode, 'city': city or
    'Not specified'}})
