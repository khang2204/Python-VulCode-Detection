@commands.command(aliases=['a9lhtob9s', 'updatea9lh'])...
"""docstring"""
embed = discord.Embed(title='Upgrading a9lh to b9s', color=discord.Color(
    13506590))
embed.set_author(name='Plailect', url='https://3ds.guide/a9lh-to-b9s')
embed.set_thumbnail(url='https://3ds.guide/images/bio-photo.png')
embed.url = 'https://3ds.guide/a9lh-to-b9s'
embed.description = (
    'A guide for upgrading your device from arm9loaderhax to boot9strap.')
await self.bot.say('', embed=embed)
