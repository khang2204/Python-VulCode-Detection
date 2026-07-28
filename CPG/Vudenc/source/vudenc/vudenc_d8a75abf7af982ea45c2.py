@commands.command(aliases=['godmode9'])...
"""docstring"""
embed = discord.Embed(title='GodMode9 Usage', color=discord.Color(6750207))
embed.set_author(name='Plailect', url='https://3ds.guide/godmode9-usage')
embed.set_thumbnail(url='https://3ds.guide/images/bio-photo.png')
embed.url = 'https://3ds.guide/godmode9-usage'
embed.description = 'GodMode9 usage guide'
await self.bot.say('', embed=embed)
