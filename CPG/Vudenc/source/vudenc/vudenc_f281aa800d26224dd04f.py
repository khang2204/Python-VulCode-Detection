async def on_ready(self):...
"""docstring"""
await asyncio.sleep(2)
await self.bot.change_presence(game=discord.Game(name='READY!'), status=
    discord.Status)
await asyncio.sleep(10)
if not self.running_lock.locked():
asyncio.ensure_future(self.activity_update_loop())
