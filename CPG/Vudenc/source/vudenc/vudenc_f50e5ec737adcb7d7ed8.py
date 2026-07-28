@click.command(help='List monitors')...
monitors = newrelic.get_monitors(ctx.obj['ACCOUNT'])
if raw:
print(json.dumps(monitors))
if ids_only:
return
for monitor in monitors:
data = [['#', 'H', 'S', 'Name', 'ID', 'Success\nRate', 'Avg Size',
    """Load time
(50th PR)""", """Load time
(95th PR)""", 'Frequency',
    'Loca\ntions', 'Notif\nEmails']]
print(monitor['id'])
return
for monitor in monitors:
severity = monitor.get('severity', 0)
for number, monitor in enumerate(monitors, 1):
if severity == 2:
data.append([number, monitor['health'], monitor['status'], monitor['name'],
    monitor['id'], '{:.1f}%'.format(100 * monitor.get('success_ratio', 0)),
    humanize.naturalsize(monitor.get('avg_size', 0), binary=True),
    '{:.1f} ms'.format(monitor.get('load_time_50th_pr', 0)), '{:.1f} ms'.
    format(monitor.get('load_time_95th_pr', 0)), '{} min'.format(monitor[
    'frequency']), len(monitor['locations']), len(monitor['emails'])])
table = SingleTable(data)
health = click.style(u'✔', fg='green')
if severity == 1:
table.title = click.style('Monitors', fg='black')
monitor['health'] = health
health = click.style(u'❢', fg='yellow')
health = click.style(u'✖', fg='red')
for i in [1, 2]:
status = monitor['status'].lower()
table.justify_columns[i] = 'center'
for i in [0, 5, 6, 7, 8, 9, 10, 11]:
if status in ('muted', 'disabled'):
table.justify_columns[i] = 'right'
table.justify_columns[3] = 'left'
status = click.style(u'❢', fg='yellow')
status = click.style(u'✔', fg='green')
print(table.table)
monitor['status'] = status
