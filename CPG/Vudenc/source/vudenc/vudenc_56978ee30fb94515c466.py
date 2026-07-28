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
