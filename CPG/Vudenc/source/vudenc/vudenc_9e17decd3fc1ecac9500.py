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
