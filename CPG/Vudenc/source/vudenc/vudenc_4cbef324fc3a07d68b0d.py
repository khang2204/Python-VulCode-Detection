@app.route('/search', methods=['GET'])...
print('in rec query')
emptyRes = {}
emptyRes['pages'] = []
print(request.args.get('query'))
query = request.args.get('query')
if not query:
return jsonify(emptyRes)
query = query.lower()
rankedList = getRanking(query)
return jsonify(rankedList)
