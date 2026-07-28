def action_delete_article(request: HttpRequest):...
"""docstring"""
u: Profile = get_current_user(request)
if 'rid' in request.GET:
if 'srid' in request.GET:
return HttpResponseRedirect(
    '/admin?error=Missing%20reservation%20id%20in%20request')
response = HttpResponseRedirect('/admin/reservations/edit?rid=' + str(int(
    request.GET['rid'])) + '&srid=' + str(int(request.GET['srid'])))
response = HttpResponseRedirect('/admin/reservations/edit?rid=' + str(int(
    request.GET['rid'])))
if request.GET.get('id'):
aid: ArticleRequested = ArticleRequested.objects.get(id=int(request.GET['id']))
return response
r: GroupReservation = GroupReservation.objects.get(id=int(request.GET['rid']))
if (aid.RID.createdByUser == u or u.rights > 1
aid.delete()
return HttpResponseRedirect(
    "/admin?error=You're%20not%20allowed%20to%20do%20this")
