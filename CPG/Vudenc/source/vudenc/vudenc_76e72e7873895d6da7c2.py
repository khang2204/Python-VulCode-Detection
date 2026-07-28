@eddb.command(aliases=['b', 'bod'])...
"""docstring"""
loop = asyncio.get_event_loop()
result = await loop.run_in_executor(None, self.body_search, inp)
await ctx.send(result)
