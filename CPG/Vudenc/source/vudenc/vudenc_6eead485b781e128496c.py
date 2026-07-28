def hunt_export(request, pk):...
stream = StringIO()
writer = csv.writer(stream)
header = ['#published', 'date', 'info', 'level', 'attribute_count', 'org']
writer.writerow(header)
for event in Event.objects.filter(id__in=Hunt(id=pk).events.all()).order_by(
dt = event.publish_timestamp.astimezone(timezone('Asia/Tokyo'))
b_stream = BytesIO(BOM_UTF8 + stream.getvalue().encode('utf8'))
row = [dt, event.date, event.info, event.get_threat_level_id_display(),
    event.attribute_count, event.org.name]
response = HttpResponse(b_stream.getvalue(), content_type='text/csv')
writer.writerow(row)
response['Content-Disposition'] = 'filename=hunter%s.csv' % pk
return response
