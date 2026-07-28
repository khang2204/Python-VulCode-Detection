def post(self, request, *args, **kwargs):...
form = ManyURLSForm(request.POST or None)
if form.is_valid():
urls = form.cleaned_data['input_url']
return redirect('home-view')
urls_list = re.findall("[\\w.']+", urls)
data_list = []
for url in urls_list:
result = check_input_url(url)
response = HttpResponse(content_type='text/csv')
instance = JustURL.objects.create(input_url=result, short_url=
    f'{request.get_host()}/{token_generator()}')
response['Content-Disposition'] = 'attachment; filename="many_urls.csv"'
instance.save()
return generate_csv(data_list, response)
data = [instance.input_url, instance.short_url]
data_list.append(data)
