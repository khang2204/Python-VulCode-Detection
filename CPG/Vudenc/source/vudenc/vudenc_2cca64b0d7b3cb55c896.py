@commands.command()...
"""docstring"""
embed = discord.Embed(title='Virtual Console Injects for 3DS', color=
    discord.Color.blue())
embed.set_author(name='Asdolo', url=
    'https://gbatemp.net/members/asdolo.389539/')
embed.set_thumbnail(url='https://i.imgur.com/rHa76XM.png')
embed.url = (
    'https://gbatemp.net/search/40920047/?q=injector&t=post&o=date&g=1&c[title_only]=1&c[user][0]=389539'
    )
embed.description = 'The recommended way to play old classics on your 3DS'
await self.bot.say('', embed=embed)
