@staticmethod...
suffixes = {'1': 'st', '2': 'nd', '3': 'rd'}
exceptions = {11, 12, 13}
if num in exceptions:
return '{:d}th'.format(num)
num = str(num)
num += suffixes.get(num[-1], 'th')
return num
