@app.route('/index', methods=['POST'])...
print(request.form)
spoofFeatures = {}
spoofFeatures['document_id'] = random.randint(1, 10000)
spoofFeatures['pagerank'] = random.random()
spoofFeatures['position'] = random.random()
spoofFeatures['frequency'] = random.random()
spoofFeatures['section'] = 'body'
spoofFeatures['date_created'] = '2018-11-05T16:18:03+0000'
spoofDocuments = {}
spoofDocuments['documents'] = []
spoofDocuments['documents'].append(spoofFeatures)
return jsonify(spoofDocuments)
