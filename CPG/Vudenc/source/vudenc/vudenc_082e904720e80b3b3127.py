def clean(self):...
super(ArticleForm, self).clean()
kw = {}
if self.cleaned_data['action'] == 'create':
return self.cleaned_data
kw['title'] = self.cleaned_data['title']
kw['content_type'] = self.cleaned_data['content_type']
kw['object_id'] = self.cleaned_data['object_id']
