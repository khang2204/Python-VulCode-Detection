@click.command(help='List accounts')...
accounts = newrelic.get_accounts()
if raw:
for account in accounts:
data = [['ID', 'Name']]
print(account[0])
for account in accounts:
data.append([account['id'], account['name']])
table = SingleTable(data)
table.title = click.style('Accounts', fg='black')
print(table.table)
