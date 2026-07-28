@commands.command()...
"""docstring"""
embed = discord.Embed(title='Check your 3DSs IP (CFW)', color=discord.Color
    .dark_orange())
embed.description = """1. FBI
2. Remote Install
3. Recieve URLs over the network"""
embed.add_field(name='Check your 3DSs IP (Homebrew)', value=
    """1. Open Homebrew Launcher
2. Press Y""")
await self.bot.say('', embed=embed)
