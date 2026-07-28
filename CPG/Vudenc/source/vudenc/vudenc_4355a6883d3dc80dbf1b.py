def validate_csp(page):...
if 'Content-Security-Policy' not in page.headers:
return False
if "default-src 'self'" not in page.headers['Content-Security-Policy']:
return False
return True
