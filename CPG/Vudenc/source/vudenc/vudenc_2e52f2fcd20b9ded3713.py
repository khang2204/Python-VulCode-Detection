def write_db_reservation_action(request: HttpRequest):...
"""docstring"""
u: Profile = get_current_user(request)
forward_url = '/admin?success'
if u.rights > 0:
forward_url = '/admin/reservations'
if request.GET.get('redirect'):
forward_url = request.GET['redirect']
if 'payload' not in request.GET:
return HttpResponseRedirect('/admin?error=No%20id%20provided')
current_reservation = GroupReservation.objects.get(id=int(request.GET[
    'payload']))
if current_reservation.createdByUser != u and u.rights < 2:
return HttpResponseRedirect('/admin?error=noyb')
current_reservation.submitted = True
current_reservation.save()
res: HttpResponseRedirect = HttpResponseRedirect(forward_url)
return res
