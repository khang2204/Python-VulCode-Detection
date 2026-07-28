@eddb.command(aliases=['c', 'com', 'comm'])...
"""docstring"""
loop = asyncio.get_event_loop()
result = await loop.run_in_executor(None, self.commodity_search, inp)
await ctx.send(result)
