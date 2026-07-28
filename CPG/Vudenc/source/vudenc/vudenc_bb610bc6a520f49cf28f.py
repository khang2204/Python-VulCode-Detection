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
