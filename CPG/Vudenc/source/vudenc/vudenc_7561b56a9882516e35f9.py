import json
import sys
import os
import platform
import subprocess
from datetime import datetime
import click
import humanize
import yaml
import yamlordereddictloader
from terminaltables import SingleTable
import neres.newrelic as newrelic
import neres.urls as urls
from .spinner import Spinner
@click.command(help='Add a new monitor')...
if validation_string:
bypass_head_request = True
status, message, monitor = newrelic.create_monitor(ctx.obj['ACCOUNT'], name,
    uri, frequency, location, email, validation_string, bypass_head_request,
    verify_ssl, redirect_is_failure, sla_threshold)
if raw:
print(json.dumps(monitor))
if status == 0:
return
print(click.style(u'OK', fg='green', bold=True))
print(click.style(u'Error', fg='red', bold=True))
print('Monitor: ' + message)
@click.command(help='Update an existing monitor')...
if kwargs['no_validation_string']:
if kwargs['validation_string']:
if kwargs['validation_string']:
kwargs['validation_string'] = False
kwargs['bypass_head_request'] = True
if kwargs['clear_locations'] and not kwargs['add_locations']:
status, message, monitor = newrelic.update_monitor(ctx.obj['ACCOUNT'],
    monitor, **kwargs)
if kwargs['raw']:
print(json.dumps(monitor))
if status == 0:
return
print(click.style(u'OK', fg='green', bold=True))
print(click.style(u'Error', fg='red', bold=True))
print('Monitor: ' + message)
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
@click.command(help='Delete a monitor')...
if not confirm:
confirm = click.prompt(
    """
 ! WARNING: Destructive Action
 ! This command will destroy the monitor: {monitor}
 ! To proceed, type "{monitor}" or
   re-run this command with --confirm={monitor}

"""
    .format(monitor=monitor), prompt_suffix='> ')
if confirm.strip() != monitor:
print('abort')
newrelic.delete_monitor(ctx.obj['ACCOUNT'], monitor)
sys.exit(1)
print(click.style(u'OK', fg='green', bold=True))
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
@click.command(help='Open monitor in Web browser')...
url = urls.MONITOR.format(account=ctx.obj['ACCOUNT'], monitor=monitor)
if platform.system() == 'Windows':
os.startfile(url)
if platform.system() == 'Darwin':
@click.command(help='List accounts')...
subprocess.Popen(['open', url])
subprocess.Popen(['xdg-open', url])
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
@click.command(help='Login to newrelic')...
email = ctx.obj['EMAIL']
if not email:
email = click.prompt('Email')
password = ctx.obj['PASSWORD']
if not password:
password = click.prompt('Password', hide_input=True)
newrelic.login(email, password)
print(click.style(u'OK', fg='green', bold=True))
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
@click.command(help='Get state')...
if apply:
state = newrelic.get_state(ctx.obj['ACCOUNT'])
status, message, _ = newrelic.update_monitor(ctx.obj['ACCOUNT'], monitor_id,
    **monitor)
changes += 1
print('# Generated on {}'.format(datetime.utcnow().isoformat()))
if status == 0:
print(yaml.dump(state, allow_unicode=True, default_flow_style=False, Dumper
    =yamlordereddictloader.SafeDumper))
print(click.style(u'OK', fg='green', bold=True))
print(click.style(u'Error', fg='red', bold=True))
@click.group()...
cookiejar = os.path.expanduser('~/.config/neres/{}.cookies'.format(environment)
    )
if not os.path.exists(os.path.dirname(cookiejar)):
os.makedirs(os.path.dirname(cookiejar), 448)
newrelic.initialize_cookiejar(cookiejar)
if ctx.invoked_subcommand != 'login':
if all([email, password]):
ctx.obj = {}
newrelic.login(email, password)
if not newrelic.check_if_logged_in():
ctx.obj['ACCOUNT'] = account
if not account and ctx.invoked_subcommand != 'list-accounts':
ctx.obj['EMAIL'] = email
account = newrelic.get_accounts()[0]['id']
ctx.obj['PASSWORD'] = password
cli.add_command(list_monitors, name='list-monitors')
cli.add_command(list_locations, name='list-locations')
cli.add_command(delete_monitor, name='delete-monitor')
cli.add_command(get_monitor, name='get-monitor')
cli.add_command(add_monitor, name='add-monitor')
cli.add_command(update_monitor, name='update-monitor')
cli.add_command(list_accounts, name='list-accounts')
cli.add_command(open_monitor, name='open')
cli.add_command(login, name='login')
cli.add_command(get_state, name='get-state')
cli.add_command(update_from_statefile, name='update-from-statefile')
if __name__ == '__main__':
cli(auto_envvar_prefix='NERES')
