def cleanID(id, isTitle):...
result = id.get('href')
if isTitle == False:
return result.split('/')[4]
if result.split('/')[3] == 'app':
return result.split('/')[5]
return 'NONE'
