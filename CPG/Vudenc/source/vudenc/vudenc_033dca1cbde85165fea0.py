@api.route('/items', methods=['GET'])...
sql = 'SELECT id, name_enus from tblDBCItem where auctionable = true;'
cursor = mysql.connection.cursor()
cursor.execute(sql)
data = cursor.fetchall()
results = []
for row in data:
item = {}
return jsonify({'items': results})
for tup in zip([column[0] for column in cursor.description], row):
item[tup[0]] = tup[1]
results.append(item)
