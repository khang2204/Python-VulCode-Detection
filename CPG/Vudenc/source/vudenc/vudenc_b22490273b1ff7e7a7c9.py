@register.simple_tag...
format_infos = {'json': {'name': 'json', 'verbose_name': 'JSON'}, 'csv': {
    'name': 'csv', 'verbose_name': 'CSV'}, 'excel.csv': {'name':
    'excel.csv', 'verbose_name': _('Excel compatible CSV')}}
return format_infos[format]
