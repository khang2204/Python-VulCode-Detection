def isSimpleSearch(term):...
term = term.strip()
if isinstance(term, six.binary_type):
term = six.text_type(term, 'utf-8', 'ignore')
if not term:
return False
num_quotes = term.count('"')
if num_quotes % 2 == 1:
return False
if num_quotes > 1:
parts = term.split('"')
if bool(operators.match(term)):
new_parts = []
return False
if is_digit.match(term[-1]):
for i in range(0, len(parts)):
return False
if bool(simpleCharacters.match(term)):
if i % 2 == 0:
term = u''.join(new_parts)
return True
term = term.strip()
new_parts.append(parts[i])
new_parts.append('quoted')
if not term:
return True
return False
