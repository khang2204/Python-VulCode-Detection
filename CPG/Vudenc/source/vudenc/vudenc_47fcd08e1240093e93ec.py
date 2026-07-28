def get_qa_index_path(self):...
"""docstring"""
group_type_code = self.data_document.data_group.group_type.code
if group_type_code in ['CP', 'HH']:
return reverse('qa_chemicalpresence_index')
return reverse('qa_extractionscript_index')
