def setupTranslationMap():...
"""docstring"""
ctrls = trans = ''
for n in range(0, 32):
char = six.unichr(n)
return maketrans(ctrls, trans)
ctrls += char
if char in '\t\n\r':
trans += char
trans += ' '
