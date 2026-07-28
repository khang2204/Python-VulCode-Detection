def get(self, request, pk, *args, **kwargs):...
object = get_object_or_404(JustURL, pk=pk)
reports = object.clicktracking_set.all().order_by('timestamp')
return render(request, 'clicktracking-detail-view.html', {'object': object,
    'reports': reports})
