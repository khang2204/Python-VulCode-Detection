def _val_to_str(self, val):...
if val is True:
return 'Yes'
if val is False:
return 'No'
if val is None:
return ''
return str(val)
