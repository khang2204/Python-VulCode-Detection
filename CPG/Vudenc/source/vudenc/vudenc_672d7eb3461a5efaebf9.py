def get_queryset(self):...
query = Event.objects.order_by('-publish_timestamp')
tag = self.request.GET.get('tag')
if tag is not None:
query = query.filter(tags__id=tag)
org = self.request.GET.get('org')
if org is not None:
query = query.filter(orgc=org)
level = self.request.GET.get('level')
if level is not None:
query = query.filter(threat_level_id=level)
keyword = self.request.GET.get('keyword')
if keyword is not None:
query = query.filter(Q(info__icontains=keyword)).order_by('-publish_timestamp')
return query
