@api.route('/item/', methods=['GET'])...
item_name = request.args.get('name')
sql = ('SELECT id, name_enus FROM `tblDBCItem` WHERE name_enus LIKE "%{}%" '
    .format(item_name))
cursor = mysql.connection.cursor()
cursor.execute(sql)
data = cursor.fetchall()
if data:
results = []
return jsonify({'error': 'item not found'}), 404
for row in data:
item = {}
return jsonify({'items': results})
for tup in zip([column[0] for column in cursor.description], row):
item[tup[0]] = tup[1]
results.append(item)
