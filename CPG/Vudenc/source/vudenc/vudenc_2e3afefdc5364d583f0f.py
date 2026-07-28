def main():...
db.create_table()
latest_update_id = None
while True:
updates = get_updates(timeout_oth, latest_update_id)
if updates['result']:
latest_update_id = get_latest_update_id(updates) + 1
time.sleep(1)
handle_updates(updates, latest_update_id)
