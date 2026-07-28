async def simple_embed(self, text, title='', color=discord.Color.default()):...
embed = discord.Embed(title=title, color=color)
embed.description = text
await self.bot.say('', embed=embed)
