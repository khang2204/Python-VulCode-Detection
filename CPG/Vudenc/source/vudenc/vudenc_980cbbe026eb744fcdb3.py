def get(self, request, pk, *args, **kwargs):...
form = CounterCountingForm()
object = JustURL.objects.get(pk=pk)
return render(request, 'url-detail-view.html', {'object': object, 'form': form}
    )
