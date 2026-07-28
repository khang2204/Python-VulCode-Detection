def get_html_val(src, name):...
if not name in src or src[name] is None:
return '-'
return src[name]
