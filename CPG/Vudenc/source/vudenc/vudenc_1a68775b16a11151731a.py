def __init__(self):...
commands = []
ro_commands_file = os.path.join(settings.config_dir, 'commands.json')
if os.path.isfile(ro_commands_file):
commands.extend(json.load(json_commands_file))
self.commands = [Command(c, readonly=True) for c in commands]
