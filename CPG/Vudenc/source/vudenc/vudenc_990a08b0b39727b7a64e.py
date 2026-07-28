async def on_connect(self):...
"""docstring"""
gateway = self.bot.ws._trace[0]
gateway = 'the gateway'
await self.bot.change_presence(game=discord.Game(name=gateway, type=2),
    status=discord.Status.dnd)
