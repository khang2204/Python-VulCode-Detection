def __init__(self, *args, **kwargs):...
super(DocumentTypeForm, self).__init__(*args, **kwargs)
self.fields['document_type'].label = ''
self.fields['document_type'].widget.attrs.update({'onchange': 'form.submit();'}
    )
