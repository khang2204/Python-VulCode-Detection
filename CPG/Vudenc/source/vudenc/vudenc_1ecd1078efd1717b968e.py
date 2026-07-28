def include_extract_form(dg):...
"""docstring"""
if not dg.type in ['FU', 'CO', 'CP']:
return False
if dg.all_matched() and not dg.all_extracted():
return ExtractionScriptForm(dg_type=dg.type)
return False
