async def save(request):...
data = await request.post()
item = Item(data['src'])
new_src = data.get('new_src')
if new_src and new_src != data['src']:
shutil.move(item.abspath, settings.STORAGE_DIR + new_src)
for field in item.FORM:
old_backup_abspath = item.backup_abspath
item.meta[field] = [data.get(field, '')]
if settings.SAVE_ORIGINALS and not os.path.isfile(item.backup_abspath):
item = Item(new_src)
shutil.copyfile(item.abspath, item.backup_abspath)
item.meta.write()
if os.path.isfile(old_backup_abspath):
return web.Response(status=200, body=json.dumps(item.get_form_fields()).
    encode('utf8'), content_type='application/json')
shutil.move(old_backup_abspath, item.backup_abspath)
