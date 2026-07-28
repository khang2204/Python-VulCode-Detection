@click.command(help='List available monitor locations')...
locations = newrelic.get_locations(ctx.obj['ACCOUNT'])
if raw:
print(json.dumps(locations))
data = [['#', 'City', 'Continent', 'Code', 'Availability', 'Accessibility']]
return
for number, location in enumerate(locations.values()):
available = click.style(u'✔', fg='green')
table = SingleTable(data)
if not location['available']:
table.title = click.style('Locations', fg='black')
click.style(u'✖', fg='red')
private = 'Private' if location['private'] else 'Public'
for i in [0, 4, 5]:
data.append([number, location['label'], location['continent'], location[
    'name'], available, private])
table.justify_columns[i] = 'right'
print(table.table)
