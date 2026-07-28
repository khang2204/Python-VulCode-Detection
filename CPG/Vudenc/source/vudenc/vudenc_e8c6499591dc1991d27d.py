def get_context_data(self, **kwargs):...
attr = Attribute.objects.all()
context = super().get_context_data(**kwargs)
context['categories'] = attr.values_list('category', flat=True).order_by(
    'category').distinct()
context['types'] = attr.values_list('type', flat=True).order_by('type'
    ).distinct()
context['count'] = self.object_list.count()
search_form = AttributeSearchForm(self.request.GET)
context['search_form'] = search_form
return context
