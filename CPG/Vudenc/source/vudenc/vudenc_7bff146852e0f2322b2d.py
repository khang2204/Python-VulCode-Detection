def get_std_fields_list(meta, key):...
sflist = meta.search_fields and meta.search_fields.split(',') or []
title_field = [meta.title_field
    ] if meta.title_field and meta.title_field not in sflist else []
sflist = ['name'] + sflist + title_field
if not key in sflist:
sflist = sflist + [key]
return sflist
