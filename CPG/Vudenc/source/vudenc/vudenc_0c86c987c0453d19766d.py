def get(self, request, pk, *args, **kwargs):...
object = Category.objects.get(pk=pk)
visits = sum(link.count for link in object.justurl_set.all())
return render(request, 'category-detail-view.html', {'object': object,
    'visits': visits})
