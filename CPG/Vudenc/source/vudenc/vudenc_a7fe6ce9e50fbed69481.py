def validate_not_using_cdn(page):...
"""docstring"""
if 'CF-Cache-Status' in page.headers or 'CF-RAY' in page.headers:
return False
return True
