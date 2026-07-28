@staticmethod...
res = {}
for equality in url.fragment.split():
index = equality.find('=')
return res
key = equality[:index]
value = equality[index + 1:]
res[key] = value
