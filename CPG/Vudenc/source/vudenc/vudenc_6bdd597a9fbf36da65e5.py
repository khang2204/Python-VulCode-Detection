def run(self, command_id):...
commands = [c for c in self.commands if c.id == command_id]
if not commands:
command = commands[0]
return command.run()
