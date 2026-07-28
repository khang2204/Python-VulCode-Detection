def different(fieldname, message=None):...
if not message:
message = 'This field needs to have a different value than ' + orm[fieldname
    ].label + '.'
def _different(form, field):...
if field.data is form[fieldname].data:
return _different
