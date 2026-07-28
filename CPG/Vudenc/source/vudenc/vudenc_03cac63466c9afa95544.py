def validate_cache_control_set(page):...
if 'Cache-Control' in page.headers:
return True
return False
