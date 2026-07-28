def cleanDate(date):...
if date == '':
return '0000-00-00'
date = date.replace(',', '')
date = date.replace('.', '')
date = date.split(' ')
if len(date) < 3:
return '0000-00-00'
if 'th' in date[1]:
result = date[2] + '-' + monthConvertor(date[0][0:3]) + '-' + date[1].replace(
    'th', '')
if date[1].isdigit():
return result
result = date[2] + '-' + monthConvertor(date[0]) + '-' + date[1]
result = date[2] + '-' + monthConvertor(date[1]) + '-' + date[0]
