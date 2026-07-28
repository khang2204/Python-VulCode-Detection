def get(self, request, format=None):...
bytesio = io.BytesIO()
zf = zipfile.ZipFile(bytesio, 'w')
for table in ['customerresponse', 'notification', 'advisor']:
csv_str = self._make_plain_csv(table)
full_csv_str = self._make_flat_wins_csv()
zf.writestr(table + 's.csv', csv_str)
zf.writestr('wins_complete.csv', full_csv_str)
full_csv_del_str = self._make_flat_wins_csv(deleted=True)
zf.writestr('wins_deleted_complete.csv', full_csv_del_str)
user_csv_str = self._make_user_csv()
zf.writestr('users.csv', user_csv_str)
zf.close()
return HttpResponse(bytesio.getvalue(), content_type=mimetypes.types_map[
    '.csv'])
