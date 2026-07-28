@commands.command(aliases=['stock115', 'stock'])...
"""docstring"""
embed = discord.Embed(title='Running stock (unmodified) 11.4+ firmware?',
    color=discord.Color.dark_orange())
embed.description = """You have 3 possible options for installing CFW:
- [NTRBoot](https://3ds.guide/ntrboot) which needs a compatible DS flashcart and maybe an additional hacked 3DS or DS(i) console depending on the flashcart
- [DSiWare](https://3ds.guide/installing-boot9strap-\\(dsiware\\)) which requires a hacked 3DS
- [Hardmod](https://3ds.guide/installing-boot9strap-\\(hardmod\\)) which requires soldering **Not for beginners!**
 **Downgrading is impossible on 11.4+!**"""
await self.bot.say('', embed=embed)
