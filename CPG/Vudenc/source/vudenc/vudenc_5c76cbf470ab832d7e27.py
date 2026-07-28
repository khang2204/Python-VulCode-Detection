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
