@commands.command()...
"""docstring"""
embed = discord.Embed(title='Fix broken TWL', color=discord.Color(10664672))
embed.set_author(name='Plailect', url=
    'https://3ds.guide/troubleshooting#twl_broken')
embed.set_thumbnail(url='https://3ds.guide/images/bio-photo.png')
embed.url = 'https://3ds.guide/troubleshooting#twl_broken'
embed.description = (
    'Instructions on how to fix a broken TWL after doing the guide')
await self.bot.say('', embed=embed)
