def get(self, request, pk, *args, **kwargs):...
object = JustURL.objects.get(pk=pk)
form = CounterCountingForm()
return render(request, 'success-url-view.html', {'object': object, 'form':
    form})
