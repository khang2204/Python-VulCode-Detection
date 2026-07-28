def get_latest_update_id(updates):...
update_ids = []
for update in updates['result']:
update_ids.append(int(update['update_id']))
latest_update_id = max(update_ids)
logging.info('get_latest_update_id: Latest update ID is %d of %s',
    latest_update_id, update_ids)
return latest_update_id
