def isSimpleTerm(term):...
if isinstance(term, six.binary_type):
term = six.text_type(term, 'utf-8', 'ignore')
term = term.strip()
simple = bool(simpleTerm.match(term))
if simple and is_digit.match(term[-1]):
return False
return simple
