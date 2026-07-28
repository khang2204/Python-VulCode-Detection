@staticmethod...
"""docstring"""
deduped_string = ''
for x in string.split(' '):
if x not in deduped_string:
return deduped_string.rstrip()
deduped_string += x + ' '
