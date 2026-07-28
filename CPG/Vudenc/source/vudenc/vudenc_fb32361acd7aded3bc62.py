@commands.command()...
"""docstring"""
embed = discord.Embed(title='Updating B9S Guide', color=discord.Color(13506590)
    )
embed.set_author(name='Plailect', url='https://3ds.guide/updating-b9s')
embed.set_thumbnail(url='https://3ds.guide/images/bio-photo.png')
embed.url = 'https://3ds.guide/updating-b9s'
embed.description = 'A guide for updating to new B9S versions.'
await self.bot.say('', embed=embed)
