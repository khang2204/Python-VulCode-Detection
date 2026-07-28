@commands.command()...
"""docstring"""
embed = discord.Embed(title='Guide - ctrtransfer', color=discord.Color.orange()
    )
embed.set_author(name='Plailect', url='https://3ds.guide/')
embed.set_thumbnail(url='https://3ds.guide/images/bio-photo.png')
embed.url = 'https://3ds.guide/ctrtransfer'
embed.description = 'How to do the 11.5.0-38 ctrtransfer'
await self.bot.say('', embed=embed)
