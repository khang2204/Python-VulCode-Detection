@commands.command()...
"""docstring"""
embed = discord.Embed(title='Sighax Information', color=discord.Color(255))
embed.set_author(name='SciresM', url=
    'https://www.reddit.com/r/3dshacks/comments/67f6as/psa_clearing_up_some_misconceptions_about_sighax/'
    )
embed.set_thumbnail(url='https://i.imgur.com/11ajkdJ.jpg')
embed.url = (
    'https://www.reddit.com/r/3dshacks/comments/67f6as/psa_clearing_up_some_misconceptions_about_sighax/'
    )
embed.description = 'PSA About Sighax'
await self.bot.say('', embed=embed)
