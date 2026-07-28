def clean(self):...
this_type = self.data_group.group_type
doc_types = DocumentType.objects.filter(group_type=this_type)
if not self.document_type in doc_types:
