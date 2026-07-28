def validate_cache_control_header(page, expected_directive):...
header = page.headers.get('Cache-Control', '')
directives = [directive.lower().strip() for directive in header.split(',')]
return expected_directive in directives
