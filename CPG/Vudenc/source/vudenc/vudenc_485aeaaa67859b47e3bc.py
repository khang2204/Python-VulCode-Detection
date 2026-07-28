def getParmeters():...
data = flask.request.json['protocoleForm']
listKeys = list()
listValues = list()
for key, value in data.iteritems():
listKeys.append(key)
return {'keys': listKeys, 'values': listValues}
listValues.append(value)
