def on_modified(event):...
if not is_background:
print('Restarting worker due to change in %s' % event.src_path)
log.info('modified %s' % event.src_path)
kill_children()
log.exception('Error while restarting worker')
run_children()
