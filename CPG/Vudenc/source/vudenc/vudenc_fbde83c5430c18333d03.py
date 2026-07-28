@commands.command()...
"""docstring"""
embed = discord.Embed(title='Dsp1', color=discord.Color.green())
embed.set_author(name='zoogie', url='https://github.com/zoogie', icon_url=
    'https://gbatemp.net/data/avatars/l/357/357147.jpg?1426471484')
embed.description = "Dump 3DS's DSP component to SD for homebrew audio."
embed.set_thumbnail(url=
    'https://raw.githubusercontent.com/Cruel/DspDump/master/icon.png')
embed.url = 'https://github.com/zoogie/DSP1/releases'
await self.bot.say('', embed=embed)
