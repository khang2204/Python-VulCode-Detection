def makeStrings(columnname, list):...
print('in makeStrings')
print(list)
if list == []:
return 'true'
result = '('
for i in range(0, len(list) - 1):
result += ' ' + columnname + " = '" + list[i] + "' or "
result += ' ' + columnname + " = '" + list[len(list) - 1] + "' ) "
print('result is ' + result)
return result
