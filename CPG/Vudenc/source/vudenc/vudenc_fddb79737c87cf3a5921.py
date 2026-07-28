def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['search_form'] = SearchForm()
filehash = self.kwargs['pk']
vt = VT()
context['vt_hash'] = vt.getFileReport(filehash)
context['vt_behavior'] = vt.getFileBehavior(filehash)
tm = ThreatMiner()
context['tm_meta'] = tm.getMetaFromSample(filehash)
context['tm_http'] = tm.getHttpFromSample(filehash)
context['tm_host'] = tm.getHostsFromSample(filehash)
context['tm_av'] = tm.getAVFromSample(filehash)
context['tm_report'] = tm.getReportFromSample(filehash)
context['events'] = Event.objects.filter(Q(info__icontains=filehash)).order_by(
    '-publish_timestamp')
count = context['events'].count()
if count > 0:
context['events_count'] = count
context['attributes'] = Attribute.objects.filter(Q(value__icontains=filehash)
    ).order_by('-timestamp')
count = context['attributes'].count()
if count > 0:
context['attributes_count'] = count
context['tws'] = tweet.objects.filter(Q(text__icontains=filehash)).order_by(
    '-datetime')
count = context['tws'].count()
if count > 0:
context['tws_count'] = count
context['exs'] = Exploit.objects.filter(Q(text__icontains=filehash)).order_by(
    '-datetime')
count = context['exs'].count()
if count > 0:
context['exs_count'] = count
return context
