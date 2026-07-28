def post(self, request, pk, *args, **kwargs):...
object = JustURL.objects.get(pk=pk)
form = CounterCountingForm(request.POST or None)
if form.is_valid():
object.count += 1
return redirect('home-view')
ip = get_client_ip(request)
client_agent = request.META['HTTP_USER_AGENT']
clicktracker = ClickTracking.objects.create(client_ip=ip, user_agent=
    client_agent)
clicktracker.url.add(object)
clicktracker.save()
object.save()
return link_redirect(request, pk)
