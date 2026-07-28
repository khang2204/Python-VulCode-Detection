def _check_rec(eview, tm):...
if eview.attrib.get('widget', False) == 'float_time':
eview.set('widget', 'float')
for child in eview:
_check_rec(child, tm)
return True
