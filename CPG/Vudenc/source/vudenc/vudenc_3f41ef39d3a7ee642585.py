@commands.command()...
"""docstring"""
embed = discord.Embed(title='Why you should not use video guides', color=
    discord.Color.dark_orange())
embed.description = """"Video guides" for custom firmware and arm9loaderhax/boot9strap are not recommended for use. Their contents generally become outdated very quickly for them to be of any use, and they are harder to update unlike a written guide.

When this happens, video guides become more complicated than current methods, having users do certain tasks which may not be required anymore.

There is also a risk of the uploader spreading misinformation or including potentially harmful files, sometimes unintentionally. Using other people's files to install arm9loaderhax can cause serious issues and even brick your system."""
embed.add_field(name='Recommended', value=
    "The recommended thing to do is to use [Plailect's written complete guide for boot9strap](https://3ds.guide). It is the most up to date one and is recommended for everyone."
    )
await self.bot.say('', embed=embed)
