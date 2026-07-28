def post(self, request, *args, **kwargs):...
form = JustURLForm(request.POST or None)
if form.is_valid():
url = form.cleaned_data['input_url']
return render(request, 'home.html', {'form': form})
short_url = form.cleaned_data['short_url']
category = form.cleaned_data['category']
if JustURL.objects.filter(short_url__contains=short_url).exists():
message = 'Token is already in use'
created = JustURL.objects.create(input_url=url, short_url=
    f'{request.get_host()}/{short_url}', category=category)
return render(request, 'custom-short-url.html', {'form': JustURLForm,
    'message': message})
created.save()
if request.user.is_superuser:
return redirect(reverse('url-detail-view', kwargs={'pk': created.pk}))
return redirect(reverse('success-url-view', kwargs={'pk': created.pk}))
