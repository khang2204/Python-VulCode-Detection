def cleanStr(str, isDiscounted):...
result = str.replace('\t', '')
result = result.replace('\r', '')
result = result.replace('\n', '')
result = result.replace('₩', '')
result = result.replace(',', '')
if result == '':
return 0
result = result.split()
if len(result) == 2 and isDiscounted:
if result[1] == 'Free':
if result[0] == 'Free':
return 0
if result[1].isdigit() == False:
return 0
if result[0].isdigit() == False:
return 0
return int(result[1])
return 0
return int(result[0])
