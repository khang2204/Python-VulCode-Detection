def sanitize_bracket(bracket, symbol='{}'):...
opn = symbol[0]
close = symbol[-1]
index = bracket.index(opn)
bracket = bracket[index:]
count = 0
for i, letter in enumerate(bracket):
if letter == opn:
bracket = bracket[:index + 1]
count = count + 1
if letter == close:
return bracket
count = count - 1
if count == 0:
index = i
