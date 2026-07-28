def extract_schema(description):...
names = []
for col in description:
names.append(col[0])
return names
