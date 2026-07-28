def get_form_kwargs(self, *args, **kwargs):...
kwargs = super().get_form_kwargs()
kwargs['entry_form_config'] = entry_form_config
question_ids = {str(q['id']) for q in entry_form_config}
data = {f'{item}': f'{value}' for item, value in self.request.GET.items() if
    item in question_ids}
if data:
kwargs['data'] = data
return kwargs
