def get_context_data(self, **kwargs):...
context = super().get_context_data(**kwargs)
context['search_form'] = SearchForm()
domain = self.kwargs['pk']
context['geoip'] = GeoIP().lookup(domain)
print(e)
context['ipaddress'] = socket.gethostbyname(domain)
vt = VT()
context['vt_domain'] = vt.getDomainReport(domain)
tm = ThreatMiner()
context['tm_url'] = tm.getURIFromDomain(domain)
context['tm_sample'] = tm.getSamplesFromDomain(domain)
context['tm_report'] = tm.getReportFromDomain(domain)
context['bls'] = blacklist.objects.filter(Q(domain=domain) | Q(
    url__contains=domain))
count = context['bls'].count()
if count > 0:
context['bls_count'] = count
context['events'] = Event.objects.filter(Q(info__icontains=domain)).order_by(
    '-publish_timestamp')
count = context['events'].count()
if count > 0:
context['events_count'] = count
context['attributes'] = Attribute.objects.filter(Q(value__icontains=domain)
    ).order_by('-timestamp')
count = context['attributes'].count()
if count > 0:
context['attributes_count'] = count
context['tws'] = tweet.objects.filter(Q(text__icontains=domain)).order_by(
    '-datetime')
count = context['tws'].count()
if count > 0:
context['tws_count'] = count
context['exs'] = Exploit.objects.filter(Q(text__icontains=domain)).order_by(
    '-datetime')
count = context['exs'].count()
if count > 0:
context['exs_count'] = count
return context
