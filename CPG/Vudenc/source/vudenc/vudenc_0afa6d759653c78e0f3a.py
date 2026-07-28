def _AddUltiSnipsDataIfNeeded(extra_data):...
if not USE_ULTISNIPS_DATA:
return
rawsnips = UltiSnips_Manager._snips('', 1)
return
extra_data['ultisnips_snippets'] = [{'trigger': x.trigger, 'description': x
    .description} for x in rawsnips]
