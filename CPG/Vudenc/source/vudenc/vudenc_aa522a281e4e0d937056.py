def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
quantity = 0
urls_without_category = JustURL.objects.filter(category=None).count()
print(urls_without_category)
queryset = Category.objects.all()
for cat in queryset:
quantity += cat.justurl_set.all().count()
context['number_of_links'] = quantity
context['urls_without_category'] = urls_without_category
return context
