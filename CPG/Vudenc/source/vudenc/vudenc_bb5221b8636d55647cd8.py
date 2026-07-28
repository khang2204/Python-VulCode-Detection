def get_extracted_template_fieldnames(self):...
extract_fields = ['data_document_id', 'data_document_filename', 'prod_name',
    'doc_date', 'rev_num', 'raw_category', 'raw_cas', 'raw_chem_name',
    'report_funcuse']
if self.type == 'FU':
return extract_fields
if self.type == 'CO':
return extract_fields + ['raw_min_comp', 'raw_max_comp', 'unit_type',
    'ingredient_rank', 'raw_central_comp']
if self.type == 'CP':
for name in ['prod_name', 'rev_num', 'report_funcuse']:
extract_fields.remove(name)
return extract_fields + ['cat_code', 'description_cpcat', 'cpcat_code',
    'cpcat_sourcetype']
