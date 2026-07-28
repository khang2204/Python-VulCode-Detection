@click.command(help='Get information for a monitor')...
monitor = newrelic.get_monitor(ctx.obj['ACCOUNT'], monitor)
if raw:
print(json.dumps(monitor))
severity = monitor.get('severity', 0)
return
if severity == 2:
health = click.style(u'✔', fg='green')
if severity == 1:
monitor['health'] = health
health = click.style(u'❢', fg='yellow')
health = click.style(u'✖', fg='red')
status = monitor['status'].lower()
if status in ('muted', 'disabled'):
status = click.style(u'❢ {}'.format(status), fg='yellow')
status = click.style(u'✔ OK', fg='green')
data = [['Monitor', monitor['id']], ['Status', status], ['Health', health],
    ['Name', monitor['name']], ['URI', monitor['uri']], ['Type', monitor[
    'type']], ['Locations', ', '.join(monitor['locations'])], [
    'slaThreshold', monitor['slaThreshold']], ['Emails', ', '.join(monitor[
    'emails'])], ['Frequency', monitor['frequency']], ['Created', monitor[
    'createdAt']], ['Modified', monitor['modifiedAt']]]
table = SingleTable(data)
table.title = click.style('Monitor', fg='black')
print(table.table)
