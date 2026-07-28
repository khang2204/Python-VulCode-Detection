@eddb.command(aliases=['sys'])...
"""docstring"""
loop = asyncio.get_event_loop()
result = await loop.run_in_executor(None, self.system_search, inp)
await ctx.send(result)
