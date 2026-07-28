def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['count'] = self.object_list.count()
context['alltag'] = Tag.objects.order_by('id')
taglist = self.request.GET.getlist('tag')
context['tags'] = Tag.objects.filter(id__in=taglist)
search_form = EventSearchForm(self.request.GET)
context['search_form'] = search_form
context['30_day_labels'] = self.thirty_day_labels()
context['30_day_data'] = self.thirty_day_data()
return context
