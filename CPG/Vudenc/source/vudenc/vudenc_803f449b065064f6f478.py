def hunt_export(request, pk):...
stream = StringIO()
writer = csv.writer(stream)
header = ['#datetime', 'user', 'screen_name', 'text']
writer.writerow(header)
for tw in tweet.objects.filter(hunt_id=Hunt(id=pk)).order_by('datetime'):
dt = tw.datetime.astimezone(timezone('Asia/Tokyo'))
b_stream = BytesIO(BOM_UTF8 + stream.getvalue().encode('utf8'))
row = [dt, tw.user, tw.screen_name, tw.text]
response = HttpResponse(b_stream.getvalue(), content_type='text/csv')
writer.writerow(row)
response['Content-Disposition'] = 'filename=hunter%s.csv' % pk
return response
