@commands.command()...
"""docstring"""
embed = discord.Embed(title='NTR Streaming Guide', color=discord.Color.blue())
embed.url = (
    'https://gbatemp.net/threads/tutorial-3ds-screen-recording-without-a-capture-card-ntr-cfw-method.423445/'
    )
embed.description = 'How to use NTR CFW with Nitro Stream to Wirelessly Stream'
embed.add_field(name='4 common fixes', value=
    """• Are you connected to the Internet?
• Is your antivirus program blocking the program?
• Make sure you are not putting the port (:####) into the IP box of Nitro Stream.
• Make sure you are on the latest preview for NTR 3.6."""
    )
await self.bot.say('', embed=embed)
