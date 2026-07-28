def getpcap(request, pk):...
response = HttpResponse(VT().getPcap(pk), content_type=
    'application/vnd.tcpdump.pcap')
response['Content-Disposition'] = 'filename=%s.pcap' % pk
return response
