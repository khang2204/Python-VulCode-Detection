@click.command(help='Login to newrelic')...
email = ctx.obj['EMAIL']
if not email:
email = click.prompt('Email')
password = ctx.obj['PASSWORD']
if not password:
password = click.prompt('Password', hide_input=True)
newrelic.login(email, password)
print(click.style(u'OK', fg='green', bold=True))
