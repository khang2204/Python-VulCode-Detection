@eddb.command(aliases=['sta'])...
"""docstring"""
loop = asyncio.get_event_loop()
result = await loop.run_in_executor(None, self.station_search, inp)
await ctx.send(result)
