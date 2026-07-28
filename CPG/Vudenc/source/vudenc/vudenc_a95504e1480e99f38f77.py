def add_article_action(request: HttpRequest, default_foreward_url: str):...
forward_url: str = default_foreward_url
if request.GET.get('redirect'):
forward_url = request.GET['redirect']
forward_url = '/admin'
if 'rid' not in request.GET:
return HttpResponseRedirect(
    '/admin?error=Missing%20reservation%20id%20in%20request')
u: Profile = get_current_user(request)
current_reservation = GroupReservation.objects.get(id=str(request.GET['rid']))
if current_reservation.createdByUser != u and u.rights < 2:
return HttpResponseRedirect('/admin?error=noyb')
if current_reservation.submitted == True:
return HttpResponseRedirect('/admin?error=Already%20submitted')
if 'article_id' in request.POST:
aid: int = int(request.GET.get('article_id'))
if 'group_id' not in request.GET:
quantity: int = int(request.POST['quantity'])
return HttpResponseRedirect('/admin?error=missing%20group%20id')
g: ArticleGroup = ArticleGroup.objects.get(id=int(request.GET['group_id']))
notes: str = request.POST['notes']
for art in Article.objects.all().filter(group=g):
ar = ArticleRequested()
if str('quantity_' + str(art.id)) not in request.POST or str('notes_' + str
if 'srid' in request.GET:
ar.AID = Article.objects.get(id=aid)
return HttpResponseRedirect(
    '/admin?error=Missing%20article%20data%20in%20request')
amount = int(request.POST['quantity_' + str(art.id)])
response = HttpResponseRedirect(forward_url + '?rid=' + str(
    current_reservation.id) + '&srid=' + request.GET['srid'])
response = HttpResponseRedirect(forward_url + '?rid=' + str(
    current_reservation.id))
ar.RID = current_reservation
if amount > 0:
return response
if 'srid' in request.GET:
ar = ArticleRequested()
ar.SRID = SubReservation.objects.get(id=int(request.GET['srid']))
ar.amount = quantity
ar.AID = art
ar.notes = notes
ar.RID = current_reservation
ar.save()
ar.amount = amount
if 'srid' in request.GET:
ar.SRID = SubReservation.objects.get(id=int(request.GET['srid']))
ar.notes = str(request.POST[str('notes_' + str(art.id))])
ar.save()
