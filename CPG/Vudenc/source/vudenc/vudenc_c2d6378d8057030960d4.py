def validate_no_cookies(page):...
if len(page.cookies.keys()) > 0:
return False
return True
