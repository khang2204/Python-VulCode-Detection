@staticmethod...
value = ''
for group in obj.groups.all():
value += group.name
return value
