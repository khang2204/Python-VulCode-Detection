def post(self, request, *args, **kwargs):...
form = ShortUrlForm(request.POST or None)
if form.is_valid():
url = form.cleaned_data['input_url']
return render(request, 'home.html', {'form': form})
category = form.cleaned_data['category']
created = JustURL.objects.create(input_url=url, category=category)
short_url = create_short_url(created)
created.short_url = f'{request.get_host()}/{short_url}'
created.save()
if request.user.is_superuser:
return redirect(reverse('url-detail-view', kwargs={'pk': created.pk}))
return redirect(reverse('success-url-view', kwargs={'pk': created.pk}))
