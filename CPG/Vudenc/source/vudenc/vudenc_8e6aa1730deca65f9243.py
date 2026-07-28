def isWildCard(term):...
if isinstance(term, six.binary_type):
term = six.text_type(term, 'utf-8', 'ignore')
return bool(wildCard.match(term))
