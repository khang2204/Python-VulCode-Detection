def validate_encoding(page):...
if page.encoding is None:
return False
if page.encoding.upper() in ('UTF-8', 'ISO-8859-1'):
return True
return False
