@api.route('/items/<int:item_id>', methods=['GET'])...
sql = (
    'SELECT id, name_enus FROM tblDBCItem WHERE id = {} AND auctionable = true;'
    .format(item_id))
cursor = mysql.connection.cursor()
cursor.execute(sql)
data = cursor.fetchone()
if data:
item = {}
return jsonify({'error': 'item not found'}), 404
for tup in zip([column[0] for column in cursor.description], data):
item[tup[0]] = tup[1]
return jsonify(item)
