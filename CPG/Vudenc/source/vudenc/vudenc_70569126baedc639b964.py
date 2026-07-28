def validate_security_header(page, header, expected_value):...
if header not in page.headers:
return False
if page.headers[header] == expected_value:
return True
return False
