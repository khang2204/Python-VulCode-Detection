@commands.command(pass_context=True)...
"""docstring"""
console = console.lower()
if console == '3ds' or console == 'auto' and 'wiiu' not in ctx.message.channel.name:
embed = discord.Embed(title='Guide', color=discord.Color(13506590))
if (console == 'wiiu' or console == 'wii u'
embed.set_author(name='Plailect', url='https://3ds.guide/')
embed = discord.Embed(title='Guide', color=discord.Color(39623))
embed.set_thumbnail(url='https://3ds.guide/images/bio-photo.png')
embed.set_author(name='FlimFlam69 & Plailect', url='https://wiiu.guide/')
embed.url = 'https://3ds.guide/'
embed.set_thumbnail(url='http://i.imgur.com/CpF12I4.png')
embed.description = (
    'A complete guide to 3DS custom firmware, from stock to boot9strap.')
embed.url = 'https://wiiu.guide/'
await self.bot.say('', embed=embed)
embed.description = (
    "FlimFlam69 and Plailect's Wii U custom firmware + coldboothax guide")
await self.bot.say('', embed=embed)
