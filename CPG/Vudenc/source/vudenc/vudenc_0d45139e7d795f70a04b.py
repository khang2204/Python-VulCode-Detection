def makeCareerAreas(list):...
if list == []:
return 'true'
result = '('
for i in range(0, len(list) - 1):
result += " maintable.careerarea = '" + list[i] + "' or "
result += " maintable.careerarea = '" + list[len(list) - 1] + "' ) "
print('result is ' + result)
return result
