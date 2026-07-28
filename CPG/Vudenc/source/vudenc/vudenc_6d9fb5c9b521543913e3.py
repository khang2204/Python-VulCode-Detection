def makeYears(list):...
if list == []:
return 'true'
result = '('
for i in range(0, len(list) - 1):
result += ' hej.year = ' + list[i] + ' or '
result += ' hej.year = ' + list[len(list) - 1] + ' ) '
return result
