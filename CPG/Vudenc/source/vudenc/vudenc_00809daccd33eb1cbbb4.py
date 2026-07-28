def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
search_form = SearchForm(self.request.GET)
context['search_form'] = search_form
count = self.object_list.count()
context['count'] = count
context['30_day_labels'] = self.thirty_day_labels()
context['30_day_data'] = self.thirty_day_data()
return context
