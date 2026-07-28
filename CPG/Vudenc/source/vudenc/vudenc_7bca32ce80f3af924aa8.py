@click.command(help='Update from state')...
if not apply:
print('This is a dry run. Run with --apply to make the changes.\n')
there_data = newrelic.get_state(ctx.obj['ACCOUNT'])
here_data = yaml.load(statefile)
changes = 0
for monitor in here_data:
for there_monitor in there_data:
if changes == 0:
if there_monitor['id'] == monitor['id']:
if there_monitor != monitor:
print('No changes made.')
print('Successfully updated {} monitors'.format(changes))
monitor_id = monitor.pop('id')
if apply:
status, message, _ = newrelic.update_monitor(ctx.obj['ACCOUNT'], monitor_id,
    **monitor)
changes += 1
if status == 0:
print(click.style(u'OK', fg='green', bold=True))
print(click.style(u'Error', fg='red', bold=True))
