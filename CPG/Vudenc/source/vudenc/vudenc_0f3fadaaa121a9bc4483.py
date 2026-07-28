def next_activity(self):...
"""docstring"""
command_choice = list(filter(lambda c: not c.qualified_name.startswith(
    'sudo'), self.bot.walk_commands()))
command = random.choice(command_choice)
return self.bot.change_presence(game=discord.Game(name=
    f'for {self.bot.command_prefix}{command.qualified_name}', type=3))
