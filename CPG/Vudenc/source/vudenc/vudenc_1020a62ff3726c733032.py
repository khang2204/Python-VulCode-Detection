@commands.command(pass_context=True, name='7zip')...
"""docstring"""
embed = discord.Embed(title='Download 7zip', color=discord.Color(255))
embed.set_thumbnail(url='http://i.imgur.com/cX1fuf6.png')
embed.url = 'http://www.7-zip.org/download.html'
embed.description = (
    'To be able to extract .7z files you need 7zip installed, get it here.')
await self.bot.say('', embed=embed)
