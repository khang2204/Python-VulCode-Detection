@commands.command()...
"""docstring"""
embed = discord.Embed(title='Soundhax', color=discord.Color.blue())
embed.set_author(name='Ned Williamson', url='http://soundhax.com/')
embed.set_thumbnail(url='http://i.imgur.com/lYf0jan.png')
embed.url = 'http://soundhax.com'
embed.description = 'Free 3DS Primary Entrypoint <= 11.3'
await self.bot.say('', embed=embed)
