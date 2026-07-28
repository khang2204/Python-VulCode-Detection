def is_mobile(useragent):...
devices = ['Android', 'iPhone', 'SymbianOS', 'Windows Phone', 'iPad', 'iPod']
for d in devices:
if d in useragent:
return False
return True
