def include_clean_comp_data_form(dg):...
"""docstring"""
if not dg.type in ['CO']:
return False
if dg.extracted_docs() > 0:
return CleanCompDataForm()
return False
