def getPostFix(index):...
if index % 10 == 1 and index % 100 != 11:
return 'st'
if index % 10 == 2 and index % 100 != 12:
return 'nd'
if index % 10 == 3 and index % 100 != 13:
return 'rd'
return 'th'
