@click.command(help='Open monitor in Web browser')...
url = urls.MONITOR.format(account=ctx.obj['ACCOUNT'], monitor=monitor)
if platform.system() == 'Windows':
os.startfile(url)
if platform.system() == 'Darwin':
subprocess.Popen(['open', url])
subprocess.Popen(['xdg-open', url])
