def manipulate_reservation_action(request: HttpRequest,...
"""docstring"""
js_string: str = ''
r: GroupReservation = None
u: Profile = get_current_user(request)
forward_url: str = default_foreward_url
if request.GET.get('redirect'):
forward_url = request.GET['redirect']
if 'srid' in request.GET:
if not request.GET.get('rid'):
if 'rid' in request.GET:
return HttpResponseRedirect('/admin?error=missing%20primary%20reservation%20id'
    )
srid: int = int(request.GET['srid'])
r = GroupReservation.objects.get(id=int(request.GET['rid']))
if u.number_of_allowed_reservations > GroupReservation.objects.all().filter(
sr: SubReservation = None
if request.POST.get('notes'):
r = GroupReservation()
return HttpResponseRedirect('/admin?error=Too%20Many%20reservations')
if srid == 0:
r.notes = request.POST['notes']
if request.POST.get('contact'):
r.createdByUser = u
sr = SubReservation()
sr = SubReservation.objects.get(id=srid)
r.responsiblePerson = str(request.POST['contact'])
if (r.createdByUser == u or o.rights > 1) and not r.submitted:
r.ready = False
if request.POST.get('notes'):
r.save()
return HttpResponseRedirect('/admin?error=noyb')
r.open = True
sr.notes = request.POST['notes']
sr.notes = ' '
response: HttpResponseRedirect = HttpResponseRedirect(forward_url + '?rid=' +
    str(r.id))
r.pickupDate = datetime.datetime.now()
sr.primary_reservation = GroupReservation.objects.get(id=int(request.GET[
    'rid']))
return response
sr.save()
print(request.POST)
print(sr.notes)
return HttpResponseRedirect('/admin/reservations/edit?rid=' + str(int(
    request.GET['rid'])) + '&srid=' + str(sr.id))
